from tkinter import *
from tkinter import ttk
import tkinter as tk
from datetime import datetime
import random
import string


class Window(tk.Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master

        super().__init__(master, bg="snow2")

        self.pack(fill=BOTH, expand = 1)

        ######## main window that contains the display screen ########

        ### titles

        welcomeMessage = Label(master, text="welcome to the password generator!", font=("Microsoft Sans Serif", 38, "bold"), bg="snow2")
        welcomeMessage.place(relx=0.5, y=173, anchor = "center")

        selectionMessage = Label(master, text="please select what you would like to include in the password:", font=("Courier", 15), bg="snow2")
        selectionMessage.place(relx=0.5, y=243, anchor = "center")


        ### checkboxes which the the user can tick and choose what they want in their password

        self.lowercase = IntVar()
        self.uppercase = IntVar()
        self.symbol = IntVar()
        self.number = IntVar()
        self.passwordlength=IntVar()

        lowercase_checkbox = Checkbutton(self, text = "lower case", onvalue = 1, offvalue = 0, variable = self.lowercase, height = 2, width = 10, font=("Consolas", 14), bg="snow2")
        lowercase_checkbox.place(relx=0.5, y=300, anchor = "center")

        uppercase_checkbox = Checkbutton(self, text = "upper case", onvalue = 1, offvalue = 0, variable = self.uppercase, height = 2, width = 10, font=("Consolas", 14), bg="snow2")
        uppercase_checkbox.place(relx=0.5, y=340, anchor = "center")

        symbol_checkbox = Checkbutton(self, text = "symbols", onvalue = 1, offvalue = 0, variable = self.symbol, height = 2, width = 10, font=("Consolas", 14), bg="snow2")
        symbol_checkbox.place(relx=0.5, y=380, anchor = "center")

        number_checkbox = Checkbutton(self, text = "numbers", onvalue = 1, offvalue = 0, variable = self.number, height = 2, width = 10, font=("Consolas", 14), bg="snow2")
        number_checkbox.place(relx=0.5, y=420, anchor = "center")


        ### textbox which allows users to enter the desired length for their password
        # length of password is stored

        lengthMessage = Label(master, text="length of password:", font=("Consolas", 16), bg="snow2")
        lengthMessage.place(x=326, y=470)

        length_input = Entry(self, width = 4, font=("Consolas", 16), textvariable=self.passwordlength)
        length_input.place(x=563, y=470)
        length_input.focus_set()


        ### generate password button will display the password after pressed in a textbox which can be edited by the user. 
        # generate_button_click is called when pressed (which calls generate_password which has the algorithm for generating the password)

        generateButton = Button(self, text = "generate", font=("Lucida Console", 15), height=1, width=10, bg = "gainsboro", activebackground = "azure3", command = self.generate_button_click)
        generateButton.place(x=265, y=530)
        self.passwordMessage = Text(self, font=("Consolas", 15), bg = "ghost white", height = 2, width = 25)
        self.passwordMessage.place(x=423, y=525)


        ### 3 different buttons for different functions: copy, save and exit
        # if copy button is pressed, copy_button_click is called which calls copy_password_to_clipboard and copies the password in the textbox to the user's keyboard
        # if save button is pressed save_button_click is called which calls save_password_to_file and will save the password in the textbox to a file which its file name is the current date and time
        # if the exit button is pressed it calls clickExitButton which exits the application
        # message will be displayed if the copy or save function was successful

        copyButton = Button(self, text = "copy", font=("Consolas", 13), height=2, width=6, command = self.copy_button_click, activebackground = "azure3")
        copyButton.place(x=380, y=600)

        saveButton = Button(self, text = "save", font=("Consolas", 13), height=2, width=6, command = self.save_button_click, activebackground = "azure3")
        saveButton.place(relx=0.5, y=626, anchor = "center")

        exitButton = Button(self, text = "exit", font=("Consolas", 13), height=2, width=6, command=self.clickExitButton, activebackground = "salmon")
        exitButton.place(x=555, y=600)

        self.success_message = Label(self, text="", font=("Consolas", 14), bg="snow2" )
        self.success_message.place(relx=0.5, y=680, anchor="center")


        ### reconfigure settings - not doing

        reconfigureSettings = Button(self, text = "--- reconfigure settings ---", font=("Consolas", 12), height=1, width=28, command = self.clickExitButton, activebackground = "azure3")
        reconfigureSettings.place(relx=0.5, y=718, anchor = "center")


        ### stars

        star = Label(master, text="☆", font=("Microsoft Sans Serif", 25, "bold"), bg="snow2")
        star.place(x=25, y=141)
        star = Label(master, text="☆", font=("Microsoft Sans Serif", 44, "bold"), bg="snow2")
        star.place(x=36, y=81)
        star = Label(master, text="⚝⚝⚝⚝⚝", font=("Microsoft Sans Serif", 23, "bold"), bg="snow2")
        star.place(x=818, y=750)


    def generate_button_click(self):
        self.generate_password()

    def generate_password(self):

        try:
            length = int(self.passwordlength.get())
        except:
            self.success_message.config(text="invalid length. please enter a positive integer", fg="firebrick1")
            return
        
        if self.passwordlength.get() == 143:
            secretMessage = Label(self, text="case 143?? why do i keep getting attracted...", font=("Microsoft Sans Serif", 13), fg="cornflower blue", bg="snow2")
            secretMessage.place(x=623, y=471)
            self.after(4000, secretMessage.destroy)

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

        if not char_pool:
            self.success_message.config(text="invalid. please select at least 1 checkbox", fg="firebrick1")
            return
            
            
        
        remaining_length = length - len(required_chars)
        password_chars = required_chars + random.choices(char_pool, k = remaining_length)
        random.shuffle(password_chars)
        self.generated_password = "".join(password_chars)

        self.passwordMessage.delete("1.0", "end")
        self.passwordMessage.insert("1.0", self.generated_password)

        self.success_message.config(text="password generated successfully", fg="SeaGreen3")
    

    def copy_button_click(self):
        current_password = self.passwordMessage.get("1.0", "end-1c")
        self.copy_password_to_clipboard(current_password)

    def copy_password_to_clipboard(self, password):
        self.clipboard_clear()
        self.clipboard_append(password)
        self.update()

        self.success_message.config(text="password copied successfully to clipboard", fg="SeaGreen3")


    def save_button_click(self):
        self.save_password_to_file(self.generated_password)

    def save_password_to_file(self, password):
        current_password = self.passwordMessage.get("1.0", "end-1c")
        current_time = datetime.now()
        fileName = current_time.strftime("%Y-%m-%d_%H.%M.%S.txt")
        with open(fileName, "wt") as f:
            f.write(current_password)
        self.success_message.config(text=f"password saved successfully to {fileName}", fg="SeaGreen3")


    def clickExitButton(self):
        exit()



root = tk.Tk()
app = Window(root)
root.wm_title("random password generator")
root.geometry("1000x800")
root.mainloop()
