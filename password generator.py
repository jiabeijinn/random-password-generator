from tkinter import *
from tkinter import ttk
import tkinter as tk
from datetime import datetime
import random
import string

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand = 1)

        welcomeMessage = Label(master, text="welcome to the password generator!", font=("Helvetica bold", 38, "bold"))
        welcomeMessage.place(relx=0.5, y=173, anchor = "center")

        selectionMessage = Label(master, text="please select what you would like to include in the password:", font=("Helvetica", 15))
        selectionMessage.place(relx=0.5, y=243, anchor = "center")


        self.lowercase = IntVar()
        self.uppercase = IntVar()
        self.symbol = IntVar()
        self.number = IntVar()
        self.passwordlength=IntVar()


        lowercase_checkbox = Checkbutton(self, text = "lower case", onvalue = 1, offvalue = 0, variable = self.lowercase, height = 2, width = 10, font=("Helvetica", 14))
        lowercase_checkbox.place(relx=0.5, y=300, anchor = "center")

        uppercase_checkbox = Checkbutton(self, text = "upper case", onvalue = 1, offvalue = 0, variable = self.uppercase, height = 2, width = 10, font=("Helvetica", 14))
        uppercase_checkbox.place(relx=0.5, y=340, anchor = "center")

        symbol_checkbox = Checkbutton(self, text = "symbols", onvalue = 1, offvalue = 0, variable = self.symbol, height = 2, width = 10, font=("Helvetica", 14))
        symbol_checkbox.place(relx=0.5, y=380, anchor = "center")

        number_checkbox = Checkbutton(self, text = "numbers", onvalue = 1, offvalue = 0, variable = self.number, height = 2, width = 10, font=("Helvetica", 14))
        number_checkbox.place(relx=0.5, y=420, anchor = "center")


        lengthMessage = Label(master, text="length of password:", font=("Helvetica", 16))
        lengthMessage.place(x=330, y=475)

        length_input = Entry(self, width = 5, font=("Helvetica", 16), textvariable=self.passwordlength)
        length_input.place(x=530, y=475)
        length_input.focus_set()


        generateButton = Button(self, text = "generate", font=("Helvetica", 15), height=1, width=10, bg = "LightCyan2", activebackground = "LightCyan3", command = self.generate_button_click)
        generateButton.place(x=265, y=530)
        self.passwordMessage = Text(self, font=("Helvetica", 15), bg = "ghost white", height = 2, width = 25)
        self.passwordMessage.place(x=423, y=525)


        copyButton = Button(self, text = "copy", font=("Helvetica", 13), height=2, width=6, command = self.copy_button_click)
        copyButton.place(x=380, y=600)

        saveButton = Button(self, text = "save", font=("Helvetica", 13), height=2, width=6, command = self.save_button_click)
        saveButton.place(relx=0.5, y=626, anchor = "center")

        exitButton = Button(self, text = "exit", font=("Helvetica", 13), height=2, width=6, command=self.clickExitButton)
        exitButton.place(x=555, y=600)

        self.success_message = Label(self, text="", font=("Helvetica", 14), fg="SeaGreen3")
        self.success_message.place(relx=0.5, y=680, anchor="center")


    def generate_button_click(self):
        self.generate_password()

    def generate_password(self):
        try:
            length = int(self.passwordlength.get())
        except ValueError:
            self.passwordMessage.config(text="invalid length")
            return


        required_chars = []
        char_pool = ""

        if self.lowercase.get():
            required_chars.append(random.choice(string.ascii_lowercase))
            char_pool += string.ascii_lowercase
        if self.uppercase.get():
            required_chars.append(random.choice(string.ascii_uppercase))
            char_pool += string.ascii_uppercase
        if self.symbol.get():
            required_chars.append(random.choice(string.punctuation))
            char_pool += string.punctuation
        if self.number.get():
            required_chars.append(random.choice(string.digits))
            char_pool += string.digits

        
        
        remaining_length = length - len(required_chars)
        password_chars = required_chars + random.choices(char_pool, k = remaining_length)
        random.shuffle(password_chars)
        self.generated_password = "".join(password_chars)
        #self.passwordMessage.config(text=self.generated_password) 
        self.passwordMessage.delete("1.0", "end")
        self.passwordMessage.insert("1.0", self.generated_password)


    def copy_button_click(self):
        current_password = self.passwordMessage.get("1.0", "end-1c")
        self.copy_password_to_clipboard(current_password)

    def copy_password_to_clipboard(self, password):
        self.clipboard_clear()
        self.clipboard_append(password)
        self.update()

        self.success_message.config(text="password copied successfully to clipboard")


    def save_button_click(self):
        self.save_password_to_file(self.generated_password)

    def save_password_to_file(self, password):
        current_password = self.passwordMessage.get("1.0", "end-1c")
        current_time = datetime.now()
        fileName = current_time.strftime("%Y-%m-%d_%H.%M.%S.txt")
        with open(fileName, "wt") as f:
            f.write(current_password)
        self.success_message.config(text=f"password saved successfully to {fileName}")


    def clickExitButton(self):
        exit()

root = Tk()
app = Window(root)
root.wm_title("random password generator")
root.geometry("1000x800")
root.mainloop()

