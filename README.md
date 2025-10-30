## 🧾 **README.md**

```markdown
# 🔐 Caesar Cipher Text Encryption & Decryption Tool

A simple yet powerful **Python-based Caesar Cipher project** featuring both **Command Line (CLI)** and **Graphical User Interface (GUI)** built with **Dear PyGui**.  
This project demonstrates the concept of classical encryption — shifting characters in text by a fixed key value to secure information.

---

## 🧠 Overview

The **Caesar Cipher** is one of the oldest and most well-known encryption algorithms.  
It replaces each letter in the plaintext with another letter a fixed number of positions down the alphabet.

For example:
```

Plain Text : HELLO
Shift Key  : 3
Cipher Text: KHOOR

```

This project allows users to both **encrypt** and **decrypt** text using a chosen shift key.

---

## 💻 Features

- 🧩 **Encrypt and Decrypt** text messages  
- 🎨 **Interactive GUI** built with Dear PyGui  
- 🧠 Simple, beginner-friendly Caesar Cipher algorithm  
- ⚙️ **Custom shift key input**  
- 🔤 Supports both uppercase and lowercase letters  
- 💬 Handles non-alphabetic characters gracefully  
- 🌗 Modern **dark theme** interface  

---

## 🧱 Project Structure

```

📁 CaesarCipherProject/
│
├── alphabet.py          # Contains the alphabet list (A–Z)
├── solver.py            # Logic for encryption & decryption
├── gui.py               # Dear PyGui interface for the project
└── README.md            # Documentation file

````

---

## ⚙️ Installation

### 1️⃣ Clone or Download the Repository
```bash
git clone https://github.com/<your-username>/caesar-cipher-project.git
cd caesar-cipher-project
````

### 2️⃣ Install Dependencies

Make sure Python is installed (version 3.8 or later).
Then install **Dear PyGui**:

```bash
pip install dearpygui
```

---

## 🚀 How to Run

### ▶️ Run the GUI version

```bash
python gui.py
```

### 💬 Run the Command Line version

```bash
python solver.py
```

---

## 🧩 How It Works

1. Enter the text you want to encrypt or decrypt.
2. Choose the mode — **Encrypt** or **Decrypt**.
3. Enter the **shift key** (e.g., 3).
4. Click **Process** to see the result.

💡 *Non-alphabetic characters (numbers, symbols, spaces) remain unchanged.*

---

## 🔒 Example Output

**Encryption:**

```
Mode: Encrypt
Message: CHATGPT
Shift: 5
Result: HMFYLUY
```

**Decryption:**

```
Mode: Decrypt
Message: HMFYLUY
Shift: 5
Result: CHATGPT
```

---

## 🧰 Technologies Used

| Tool             | Description                      |
| ---------------- | -------------------------------- |
| 🐍 Python        | Programming language             |
| 🎨 Dear PyGui    | GUI framework                    |
| 🔡 Caesar Cipher | Classical cryptography algorithm |

---

## 🧠 Learning Outcomes

* Understanding classical encryption (Caesar Cipher)
* Working with Python strings and loops
* Building a GUI with Dear PyGui
* Handling user input and exceptions
* Combining logic with interface design

---

## 💡 Future Improvements

* Add **file encryption/decryption** support
* Allow **custom themes** and color selection
* Show **real-time output preview**
* Add **copy-to-clipboard** feature for results

---

## 👨‍💻 Author

**Muaaz Tariq**
🎓 *Student Project – Viva Submission*
💬 Built using Python and Dear PyGui


```

