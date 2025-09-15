# 🔑 Known-Word Decryptor

A simple Python tool that decrypts a Caesar cipher text when you know **at least one word** from the original plaintext.  
It works by deducing the shift number from the known word and then decrypting the entire encrypted text.

---

## ✨ Features
- Automatically detects the Caesar cipher shift using a known word
- Supports both uppercase and lowercase text
- Preserves punctuation (.,!?')
- Works with single-letter or multi-letter known words
- Simple, lightweight, and easy to extend

---

## 📦 Installation
Clone the repository and navigate into it:
```bash
git clone https://github.com/Karmscript/Encryption_challenge
cd plain_text_decryption
No additional dependencies are required — it’s pure Python!

##🖥 Usage
You can import the function or run it in a script.
Example:


from Encryption_challenge import plain_text_decryption

Encrypted = "Nz obnf jt Cbssz Bmmfo, boe J bn uif gbtuftu nbo bmjwf."
KnownWord = "My"

decrypted_text = decrypt(Encrypted, KnownWord)
print(decrypted_text)
Output:My name is Barry Allen, and I am the fastest man alive.

##Future Ideas
Support for multiple known words

Detect shift without a known word using frequency analysis

Web interface or CLI tool

##📄 License
MIT License — feel free to use, modify, and share.
