import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 1:
            messagebox.showerror("Invalid Input", "Password length must be at least 1.")
            return
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        
        result_label.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the length.")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_label.cget("text").replace("Generated Password: ", ""))
    messagebox.showinfo("Copied", "Password copied to clipboard")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

instructions_label = tk.Label(root, text="Enter the desired password length:", font=('Arial', 14))
instructions_label.pack(pady=10)

length_entry = tk.Entry(root, font=('Arial', 14))
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", font=('Arial', 14), command=generate_password)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=('Arial', 14))
result_label.pack(pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", font=('Arial', 14), command=copy_to_clipboard)
copy_button.pack(pady=10)

root.mainloop()
