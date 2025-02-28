import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import random
import string

# Main Application Window
root = tk.Tk()
root.title("Password Generator & Text Editor")
root.geometry("700x550")
root.resizable(False, False)

# Set Style for a Modern Look
style = ttk.Style()
style.configure("TFrame", background="#2C2F33")
style.configure("TLabel", background="#2C2F33", foreground="white", font=("Arial", 10, "bold"))
style.configure("TButton", background="#7289DA", foreground="black", font=("Arial", 10, "bold"))
style.configure("TEntry", font=("Arial", 10))

# -------------------- PASSWORD GENERATOR --------------------

def generate_password():
    length = int(password_length.get())
    if length < 4:
        messagebox.showerror("Error", "Password length must be at least 4")
        return

    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(chars) for _ in range(length))
    password_var.set(password)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")

def save_password():
    password = password_var.get()
    website = website_entry.get()
    username = username_entry.get()

    if not password or not website or not username:
        messagebox.showerror("Error", "Please enter website, username, and generate a password before saving.")
        return

    save_path = "saved_passwords.txt"
    with open(save_path, "a") as file:
        file.write(f"Website: {website} | Username: {username} | Password: {password}\n")

    messagebox.showinfo("Success", "Password saved successfully!")

def toggle_password():
    if password_entry.cget('show') == "*":
        password_entry.config(show="")
        toggle_btn.config(text="🙈 Hide")
    else:
        password_entry.config(show="*")
        toggle_btn.config(text="👁 Show")

# Password Generator Frame
password_frame = ttk.LabelFrame(root, text="🔐 Password Generator", padding=10)
password_frame.pack(fill="x", padx=10, pady=10)

ttk.Label(password_frame, text="Website:").grid(row=0, column=0, padx=5, pady=5)
website_entry = ttk.Entry(password_frame, width=20)
website_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(password_frame, text="Username:").grid(row=0, column=2, padx=5, pady=5)
username_entry = ttk.Entry(password_frame, width=20)
username_entry.grid(row=0, column=3, padx=5, pady=5)

ttk.Label(password_frame, text="Length:").grid(row=1, column=0, padx=5, pady=5)
password_length = ttk.Entry(password_frame, width=5)
password_length.insert(0, "12")
password_length.grid(row=1, column=1, padx=5, pady=5)

generate_btn = ttk.Button(password_frame, text="Generate", command=generate_password)
generate_btn.grid(row=1, column=2, padx=5, pady=5)

password_var = tk.StringVar()
password_entry = ttk.Entry(password_frame, textvariable=password_var, width=20, state="readonly", show="*")
password_entry.grid(row=1, column=3, padx=5, pady=5)

toggle_btn = ttk.Button(password_frame, text="👁 Show", command=toggle_password)
toggle_btn.grid(row=1, column=4, padx=5, pady=5)

copy_btn = ttk.Button(password_frame, text="Copy", command=copy_password)
copy_btn.grid(row=2, column=2, padx=5, pady=5)

save_btn = ttk.Button(password_frame, text="Save", command=save_password)
save_btn.grid(row=2, column=3, padx=5, pady=5)

# -------------------- TEXT EDITOR (Dark Themed) --------------------

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", ".txt"), ("All Files", ".*")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", ".txt"), ("All Files", ".*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))

# Text Editor Frame
text_frame = ttk.LabelFrame(root, text="📝 Text Editor", padding=10)
text_frame.pack(fill="both", expand=True, padx=10, pady=10)

text_area = tk.Text(text_frame, wrap="word", height=12, bg="#23272A", fg="white", insertbackground="white", font=("Courier", 12))
text_area.pack(fill="both", expand=True, padx=5, pady=5)

# Buttons for Text Editor
button_frame = ttk.Frame(root)
button_frame.pack(fill="x", padx=10, pady=5)

open_btn = ttk.Button(button_frame, text="📂 Open", command=open_file)
open_btn.pack(side="left", padx=5)

save_btn = ttk.Button(button_frame, text="💾 Save", command=save_file)
save_btn.pack(side="left", padx=5)

clear_btn = ttk.Button(button_frame, text="🗑 Clear", command=lambda: text_area.delete(1.0, tk.END))
clear_btn.pack(side="left", padx=5)

# Run Application
root.mainloop()