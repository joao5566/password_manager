import tkinter as tk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
# window.minsize(300, 700)
window.configure(padx=20, pady=20)
window.title("Password Manager")

logo_img = tk.PhotoImage(file="logo.png")
# ----- configuração do canvas----------#
canvas = tk.Canvas(
    width=200,
    height=200,
)

canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


# -------- formulario --------------#

website_label = tk.Label()
website_label.config(text="Website")
website_label.grid(column=2, row=1)

website_entry = tk.Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, padx=5, pady=5)


email_user_label = tk.Label()
email_user_label.config(text="Email/Username:")
email_user_label.grid(column=0, row=2, padx=5, pady=5)

email_user_entry = tk.Entry(width=35)
email_user_entry.grid(column=1, row=2, columnspan=2, padx=5, pady=5)

password_label = tk.Label()
password_label.config(text="Password")
password_label.grid(column=0, row=3, padx=5, pady=5)

password_entry = tk.Entry(width=21)
password_entry.grid(column=1, row=3, padx=5, pady=5)

generate_pass_btn = tk.Button()
generate_pass_btn.config(text="Generate", width=10)
generate_pass_btn.grid(column=2, row=3)

add_button = tk.Button()
add_button.config(text="add", width=35)
add_button.grid(column=1, row=4, columnspan=2, pady=5, padx=4)

window.mainloop()
