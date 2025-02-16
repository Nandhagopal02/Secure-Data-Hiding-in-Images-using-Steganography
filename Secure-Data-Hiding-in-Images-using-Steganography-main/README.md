# Image Steganography (Encrypt & Decrypt Messages in Images)

## 📌 Project Overview
This project implements **image-based steganography** that allows users to securely **hide and retrieve secret messages** inside an image using a password. The graphical user interface (GUI) is built using **Tkinter**, and the image processing is handled with **OpenCV**.

## 🛠 Features
- **Encrypt a Secret Message** 🔐
  - Hide a message inside an image without changing its appearance.
  - Protect the message with a password.
- **Decrypt the Message** 🔓
  - Extract the hidden message from the image.
  - Requires the correct password for successful decryption.
- **GUI-based Interface** 🖥️
  - Simple and easy-to-use GUI for encryption and decryption.
  - Colorful and responsive design.

## 📂 Project Structure
```
📁 Image-Steganography-Project
│-- encrypt_image.py  # GUI for encrypting messages in an image
│-- decrypt_image.py  # GUI for decrypting messages from an image
│-- README.md         # Project documentation

## 🚀 Installation & Setup
### 1️⃣ Install Dependencies
Make sure you have **Python 3.6+** installed. Then, install the required libraries:
```bash
pip install opencv-python tkinter
```

### 2️⃣ Run the Encryption Script
To encrypt a message into an image:
```bash
python encrypt_image.py
```
- Select an image.
- Enter a secret message.
- Enter a password.
- Save the encrypted image.

### 3️⃣ Run the Decryption Script
To decrypt a message from an image:
```bash
python decrypt_image.py
```
- Select the encrypted image.
- Enter the correct password.
- Retrieve the hidden message.

## ⚡ Usage
### 🔹 Encrypting a Message
1. Select an image file.
2. Enter your secret message.
3. Enter a password for protection.
4. Click **Encrypt** → Save the encrypted image.

### 🔹 Decrypting a Message
1. Select the encrypted image file.
2. Enter the correct password.
3. Click **Decrypt** → The message is displayed.

## 🛡 Security Considerations
- The message is hidden at the pixel level but is **not strongly encrypted**.
- For added security, use additional cryptographic encryption (e.g., AES) before encoding.
- If the password is incorrect, decryption will fail.

## 📌 Future Enhancements
- 🔄 **Support for multiple image formats** (JPEG, PNG, etc.).
- 🔑 **Stronger encryption methods** for added security.
- 📱 **Mobile app version** using Python-Kivy or Flutter.

## 💡 Credits
Developed using:
- **Python** 🐍
- **OpenCV** 📷
- **Tkinter** 🖥️
