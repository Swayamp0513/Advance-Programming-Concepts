
import tkinter as tk
from tkinter import messagebox
import re


def register():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    phone = phone_entry.get().strip()
    password = password_entry.get()
    confirm_password = confirm_entry.get()
    gender = gender_var.get()

    # 1. Check empty fields
    if not name or not email or not phone or not password or not confirm_password:
        messagebox.showerror("Error", "All fields are required!")
        return

    # 2. Validate name
    if not name.replace(" ", "").isalpha():
        messagebox.showerror("Error", "Name must contain letters only!")
        return

    # 3. Validate email
    email_pattern = r"^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$"
    if not re.match(email_pattern, email):
        messagebox.showerror("Error", "Please enter a valid email address!")
        return

    # 4. Validate phone number (exactly 10 digits)
    if not re.fullmatch(r"[0-9]{10}", phone):
        messagebox.showerror(
            "Error",
            "Phone number must contain exactly 10 digits!"
        )
        return

    # 5. Validate password length
    if len(password) < 8:
        messagebox.showerror(
            "Error", "Password must be at least 8 characters!"
        )
        return

    # 6. Check password confirmation
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    # 7. Validate gender
    if not gender:
        messagebox.showerror("Error", "Please select your gender!")
        return

    # Registration successful
    messagebox.showinfo(
        "Success",
        f"Registration successful!\n\n"
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Phone: {phone}\n"
        f"Gender: {gender}"
    )

    # Clear form
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    confirm_entry.delete(0, tk.END)
    gender_var.set("")


# Main window
root = tk.Tk()
root.title("Registration Form with Validation")
root.geometry("400x550")
root.configure(bg="#f0f4f8")
root.resizable(False, False)

# Heading
tk.Label(
    root,
    text="Registration Form",
    font=("Arial", 18, "bold"),
    bg="#f0f4f8",
    fg="#1d3557"
).pack(pady=15)

# Full name
tk.Label(root, text="Full Name", bg="#f0f4f8").pack()
name_entry = tk.Entry(root, width=35)
name_entry.pack(pady=5)

# Email
tk.Label(root, text="Email Address", bg="#f0f4f8").pack()
email_entry = tk.Entry(root, width=35)
email_entry.pack(pady=5)

# Phone number
tk.Label(root, text="Phone Number", bg="#f0f4f8").pack()
phone_entry = tk.Entry(root, width=35)
phone_entry.pack(pady=5)

# Password
tk.Label(root, text="Password", bg="#f0f4f8").pack()
password_entry = tk.Entry(root, width=35, show="*")
password_entry.pack(pady=5)

# Confirm password
tk.Label(root, text="Confirm Password", bg="#f0f4f8").pack()
confirm_entry = tk.Entry(root, width=35, show="*")
confirm_entry.pack(pady=5)

# Gender
tk.Label(root, text="Gender", bg="#f0f4f8").pack(pady=(8, 2))
gender_var = tk.StringVar(value="")

gender_frame = tk.Frame(root, bg="#f0f4f8")
gender_frame.pack()

for option in ["Male", "Female", "Other"]:
    tk.Radiobutton(
        gender_frame,
        text=option,
        variable=gender_var,
        value=option,
        bg="#f0f4f8"
    ).pack(side=tk.LEFT, padx=5)

# Register button
tk.Button(
    root,
    text="Register",
    command=register,
    bg="green",
    fg="white",
    font=("Arial", 11, "bold"),
    width=15
).pack(pady=20)

root.mainloop()
