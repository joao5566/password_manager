import tkinter as tk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.minsize(800, 700)
window.configure(padx=20, pady=20)
window.title("Password Manager")

canvas = tk.Canvas(
    width=200,
    height=200,
)

window.mainloop()

