import cv2
import tkinter as tk
from tkinter import filedialog, messagebox

def decrypt_image(image_path, entered_password):
    img = cv2.imread(image_path)
    if img is None:
        messagebox.showerror("Error", "Unable to read the image file.")
        return

    c = {i: chr(i) for i in range(255)}

    # Retrieve message length
    message_length = img[0, 0, 0]
    if message_length == 0:
        messagebox.showerror("Error", "No encrypted message found!")
        return

    message = ""
    n, m, z = 0, 1, 0  # Start from second pixel

    for _ in range(message_length):
        message += c.get(img[n, m, z], "?")  # Default to '?'
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m >= img.shape[1]:
                m = 0
                n += 1

    # Check message format
    if ":" not in message:
        messagebox.showerror("Error", "Decryption failed! Data may be corrupted.")
        return

    # Split password and message
    stored_password, decrypted_message = message.split(":", 1)

    if stored_password == entered_password:
        messagebox.showinfo("Decrypted Message", decrypted_message)
    else:
        messagebox.showerror("Error", "Incorrect Password")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        entry_image_path.delete(0, tk.END)
        entry_image_path.insert(0, file_path)

def decrypt_action():
    image_path = entry_image_path.get()
    entered_password = entry_password.get()

    if not image_path:
        messagebox.showwarning("Warning", "Please select an encrypted image!")
        return
    
    if not entered_password:
        messagebox.showwarning("Warning", "Please enter a password!")
        return

    decrypt_image(image_path, entered_password)

# GUI Setup
root = tk.Tk()
root.title("Image Decryption")
root.geometry("500x300")
root.configure(bg="#2C3E50")

# Configure grid layout
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)

# Title Label
tk.Label(root, text="Image Decryption Tool", bg="#2C3E50", fg="white", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=3, pady=10)

# Select Image
tk.Label(root, text="Select Encrypted Image:", bg="#2C3E50", fg="white", font=("Arial", 10)).grid(row=1, column=0, padx=10, sticky="e")
entry_image_path = tk.Entry(root, width=40)
entry_image_path.grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=browse_file, bg="#1ABC9C", fg="white", width=10).grid(row=1, column=2, padx=10)

# Password Field
tk.Label(root, text="Enter Password:", bg="#2C3E50", fg="white", font=("Arial", 10)).grid(row=2, column=0, padx=10, sticky="e")
entry_password = tk.Entry(root, show="*", width=40)
entry_password.grid(row=2, column=1, padx=10, pady=5)

# Decrypt Button
tk.Button(root, text="Decrypt", command=decrypt_action, bg="#E74C3C", fg="white", width=15).grid(row=3, column=0, columnspan=3, pady=15)

root.mainloop()
