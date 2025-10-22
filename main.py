import json
import os
import random
import sys
import tkinter as tk
from tkinter import END, Button, Message, messagebox
import pyperclip
import json

# ESSA FUNÇÃO É ESSENCIAL
def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

    # ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    # Password Generator Project
    letters = [
        "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w",
        "x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


    
def save():

    def open_json(file, mode = "r", data = {}):
        if mode.lower() == "w":
            with open(file, "w") as file:
                json.dump(data,file,indent=4)
        elif mode.lower() == "r":
            with open(file, "r") as file:
                return json.load(file)
            
    
    website = website_entry.get()
    email = email_user_entry.get()
    password = password_entry.get()
    
    new_data = {
            website:{
                "email": email,
                "password":password,
                }
            }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Ooops", message="Please make sure you haven't left any fields empty."
        )
    else:
        try:
            data = open_json("data.json","r")  
            data.update(new_data)
            open_json("data.json","w",data)
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)            
        except FileNotFoundError:
            open_json("data.json","w",new_data)
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)


            

#--------------------Search password ---------------------------------#
def search_pass():
    try:
        with open("data.json","r") as file:
            open_file= json.load(file)
            website = website_entry.get()
            pyperclip.copy(open_file[website]["password"])
            messagebox.showinfo(title=f"{website}",message=f"Email: {open_file[website]["email"]}\n Password: {open_file[website]["password"]}")

    except KeyError:
       messagebox.showinfo(title="Ooops",message="password not found") 
    except FileNotFoundError:
        messagebox.showinfo("Ooops",message="you don't have any saved passwords yet")
    
# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
# window.minsize(300, 700)
window.configure(padx=60, pady=60)
window.title("Password Manager")

logo_img = tk.PhotoImage(file=resource_path("img/logo.png"))
# ----- configuração do canvas----------#
canvas = tk.Canvas(
    width=200,
    height=200,
)

canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


# -------- formulario --------------#


website_label = tk.Label()
website_label.config(text="Website:")
website_label.grid(column=0, row=1)

website_entry = tk.Entry(width=21)
website_entry.focus()
website_entry.grid(column=1, row=1)

search_btn = tk.Button()
search_btn.config(text="Search",command=search_pass)
search_btn.grid(column=2, row=1)

email_user_label = tk.Label()
email_user_label.config(text="Email/Username:")
email_user_label.grid(column=0, row=2, padx=5, pady=5)

email_user_entry = tk.Entry(width=35)
email_user_entry.insert(0, "email@email.com")
email_user_entry.grid(column=1, row=2, columnspan=2, padx=5, pady=5)

password_label = tk.Label()
password_label.config(text="Password:")
password_label.grid(column=0, row=3, padx=5, pady=5)

password_entry = tk.Entry(width=21)
password_entry.grid(column=1, row=3, padx=5, pady=5)

generate_pass_btn = tk.Button()
generate_pass_btn.config(text="Generate", command=generate_password)
generate_pass_btn.grid(column=2, row=3, padx=5, pady=5)

add_button = tk.Button()
add_button.config(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2, pady=5, padx=4)

window.mainloop()
