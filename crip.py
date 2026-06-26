from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"

# Create a key if it doesn't exist
if not os.path.exists(KEY_FILE):
    with open(KEY_FILE, "wb") as f:
        f.write(Fernet.generate_key())

# Load the key
with open(KEY_FILE, "rb") as f:
    key = f.read()

cipher = Fernet(key)

def encrypt():
    text = text_box.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Enter some text.")
        return

    encrypted = cipher.encrypt(text.encode()).decode()

    result_box.config(state="normal")
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, encrypted)
    result_box.config(state="disabled")

def decrypt():
    text = text_box.get("1.0", tk.END).strip()

    try:
        decrypted = cipher.decrypt(text.encode()).decode()

        result_box.config(state="normal")
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, decrypted)
        result_box.config(state="disabled")

    except Exception:
        messagebox.showerror("Error", "Invalid encrypted text.")

root = tk.Tk()
root.title("Encryption & Decryption Tool")
root.config(bg="#D4D3D4")
root.geometry("600x450")

tk.Label(root, text="Input").pack()

text_box = tk.Text(root, height=8)
text_box.pack(fill="both", padx=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)
tk.Button(button_frame, text="Encrypt", command=encrypt).pack(side="left", padx=10)
tk.Button(button_frame, text="Decrypt", command=decrypt).pack(side="left", padx=10)

tk.Label(root, text="Output").pack()

result_box = tk.Text(root, height=8, state="disabled")
result_box.pack(fill="both", padx=10)

root.mainloop()

# key=Fernet.generate_key()
# msg=input("enter a message which you want to encrypt").encode()
# f_obj=Fernet(key)
# encrypted_message=f_obj.encrypt(msg)
# print(encrypted_message)
# decrypted_message=f_obj.decrypt(encrypted_message)
# print(decrypted_message)