import os
import sys
import tkinter as tk
from tkinter import messagebox


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

    # ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_user_entry.get()
    password = password_entry.get()

    if len(password) <= 0:
        messagebox.showerror(title="Burro", message="Você não colocou a senha anta")
    elif len(website) <= 0:
        messagebox.showerror(title="Burro", message="Você não colocou o site anta")
    elif len(email) <= 0:
        messagebox.showerror(title="Burro", message="Você não colocou a email  anta")
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are  the details entered \n {email} \n{password} \nis it ok to save?",
        )

        if is_ok:
            with open("password.txt", "a+") as file:
                file.write(f"{website} | {email} | {password}")
                website_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)


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

website_entry = tk.Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, padx=5, pady=5)


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
generate_pass_btn.config(text="Generate")
generate_pass_btn.grid(column=2, row=3, padx=5, pady=5)

add_button = tk.Button()
add_button.config(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2, pady=5, padx=4)

window.mainloop()
