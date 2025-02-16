import cv2
import tkinter as tk
from tkinter import filedialog, messagebox

def encrypt_image(image_path, secret_message, password):
    img = cv2.imread(image_path)
    if img is None:
        messagebox.showerror("Error", "Unable to read the image file.")
        return

    full_message = password + ":" + secret_message  # Store password and message
    message_length = len(full_message)

    if message_length > img.shape[0] * img.shape[1]:
        messagebox.showerror("Error", "Message is too long for the image.")
        return

    d = {chr(i): i for i in range(255)}

    img[0, 0, 0] = message_length  # Store message length in first pixel

    n, m, z = 0, 1, 0  # Start from second pixel
    for char in full_message:
        img[n, m, z] = d.get(char, 63)  # Encode character (default '?' if missing)
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m >= img.shape[1]:
                m = 0
                n += 1

    encrypted_path = "encrypted_image.png"
    cv2.imwrite(encrypted_path, img)
    messagebox.showinfo("Success", f"Image encrypted and saved as {encrypted_path}")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        entry_image_path.delete(0, tk.END)
        entry_image_path.insert(0, file_path)

def encrypt_action():
    image_path = entry_image_path.get()
    secret_message = entry_message.get()
    password = entry_password.get()

    if not image_path:
        messagebox.showwarning("Warning", "Please select an image!")
        return
    
    if not secret_message:
        messagebox.showwarning("Warning", "Please enter a secret message!")
        return

    if not password:
        messagebox.showwarning("Warning", "Please enter a password!")
        return

    encrypt_image(image_path, secret_message, password)

# GUI Setup
root = tk.Tk()
root.title("Image Encryption")
root.geometry("500x300")
root.configure(bg="#2C3E50")

# Configure grid layout
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)

# Title Label
tk.Label(root, text="Image Encryption Tool", bg="#2C3E50", fg="white", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=3, pady=10)

# Select Image
tk.Label(root, text="Select Image:", bg="#2C3E50", fg="white", font=("Arial", 10)).grid(row=1, column=0, padx=10, sticky="e")
entry_image_path = tk.Entry(root, width=40)
entry_image_path.grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=browse_file, bg="#1ABC9C", fg="white", width=10).grid(row=1, column=2, padx=10)

# Secret Message Field
tk.Label(root, text="Enter Secret Message:", bg="#2C3E50", fg="white", font=("Arial", 10)).grid(row=2, column=0, padx=10, sticky="e")
entry_message = tk.Entry(root, width=40)
entry_message.grid(row=2, column=1, padx=10, pady=5)

# Password Field
tk.Label(root, text="Enter Password:", bg="#2C3E50", fg="white", font=("Arial", 10)).grid(row=3, column=0, padx=10, sticky="e")
entry_password = tk.Entry(root, show="*", width=40)
entry_password.grid(row=3, column=1, padx=10, pady=5)

# Encrypt Button
tk.Button(root, text="Encrypt", command=encrypt_action, bg="#E74C3C", fg="white", width=15).grid(row=4, column=0, columnspan=3, pady=15)

root.mainloop()
