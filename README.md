# Encryption & Decryption Tool

## Overview

The **Encryption & Decryption Tool** is a simple desktop application built using **Python**, **Tkinter**, and the **Cryptography (Fernet)** library. It provides a graphical user interface (GUI) that allows users to securely encrypt and decrypt text using symmetric-key encryption.

The application automatically generates and stores a secret encryption key (`secret.key`) during its first execution. This key is then reused to decrypt any text encrypted by the application.

---

## Features

* Encrypt plain text using the Fernet encryption algorithm.
* Decrypt previously encrypted text.
* Automatically generates a secret key if one does not exist.
* User-friendly graphical interface built with Tkinter.
* Displays error messages for invalid encrypted data.
* Secure encryption using the Cryptography library.

---

## Technologies Used

* Python 3.x
* Tkinter (GUI)
* Cryptography (Fernet)
* OS module

---

## Project Structure

```
Encryption-Decryption-Tool/
│
├── main.py          # Main Python program
├── secret.key       # Automatically generated encryption key
└── README.md        # Project documentation
```

---

## Installation

### 1. Clone or Download the Project

```bash
git clone https://github.com/yourusername/encryption-decryption-tool.git
```

or download the ZIP file and extract it.

### 2. Install Required Package

```bash
pip install cryptography
```

Tkinter is included with most Python installations.

---

## How to Run

Run the following command:

```bash
python main.py
```

The graphical application window will open.

---

## How to Use

### Encrypt Text

1. Enter plain text into the **Input** box.
2. Click the **Encrypt** button.
3. The encrypted text will appear in the **Output** box.

### Decrypt Text

1. Copy the encrypted text.
2. Paste it into the **Input** box.
3. Click the **Decrypt** button.
4. The original text will appear in the **Output** box.

---

## How It Works

* When the application starts, it checks whether a file named `secret.key` exists.
* If the file is missing, a new Fernet key is generated and saved.
* The key is loaded into memory.
* During encryption:

  * The input text is converted into bytes.
  * Fernet encrypts the data.
  * The encrypted text is displayed.
* During decryption:

  * The encrypted text is decrypted using the same secret key.
  * If the text or key is invalid, an error message is displayed.

---

## Security Notes

* Keep the `secret.key` file safe.
* If the key file is deleted or replaced, previously encrypted messages cannot be decrypted.
* Anyone with access to the `secret.key` file can decrypt your encrypted data.

---

## Example

### Input

```
Hello World
```

### Encrypted Output

```
gAAAAABoXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

### Decrypted Output

```
Hello World
```

---

## Future Improvements

* Save encrypted text to a file.
* Open encrypted files directly.
* Copy encrypted/decrypted text with one click.
* Password-protect the encryption key.
* Support drag-and-drop file encryption.
* Add dark mode and improved UI styling.

---

## Author

**Name:** *Manshi Chauhan*

---

## License

This project is open source and available under the MIT License.
