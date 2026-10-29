
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Registration Form")
root.geometry("400x500")
root.configure(bg="lightblue")

# Heading
tk.Label(
    root,
    text="Registration Form",
    font=("Arial", 20, "bold"),
    bg="lightblue"
).pack(pady=15)

# Form fields
fields = ["Full Name", "Email", "Phone Number", "Username", "Password"]
entries = {}

for field in fields:
    tk.Label(
        root, text=field, bg="lightblue",
        font=("Arial", 11)
    ).pack()

    entry = tk.Entry(root, width=30)
    entry.pack(pady=5)
    entries[field] = entry

# Gender
tk.Label(root, text="Gender", bg="lightblue").pack(pady=3)

gender = tk.StringVar(value="Male")

tk.OptionMenu(root, gender, "Male", "Female", "Other").pack()

# Register button
def register():
    details = ""

    for field, entry in entries.items():
        details += f"{field}: {entry.get()}\n"

    details += f"Gender: {gender.get()}"

    messagebox.showinfo(
        "Registration Successful",
        "Registration Successful!\n\n" + details
    )

tk.Button(
    root,
    text="Register",
    command=register,
    bg="green",
    fg="white",
    font=("Arial", 12, "bold")
).pack(pady=20)

root.mainloop()
