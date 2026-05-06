# Practical 6 - Monoalphabetic and Polyalphabetic (Vigenere) Cipher

import random, string

# --- Monoalphabetic ---
text = input("Enter text: ").upper()

alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
shuffled = alpha.copy()
random.shuffle(shuffled)

encrypted = ""
for ch in text:
    if ch.isalpha():
        encrypted += shuffled[ord(ch) - 65]
    else:
        encrypted += ch

decrypted = ""
for ch in encrypted:
    if ch.isalpha():
        decrypted += alpha[shuffled.index(ch)]
    else:
        decrypted += ch

print("\n-- Monoalphabetic Cipher --")
print("Key       :", ''.join(shuffled))
print("Original  :", text)
print("Encrypted :", encrypted)
print("Decrypted :", decrypted)

# --- Polyalphabetic (Vigenere) ---
keyword = input("\nEnter keyword for Vigenere: ").upper()
text2 = input("Enter text: ").upper()

enc2 = ""
i = 0
for ch in text2:
    if ch.isalpha():
        shift = ord(keyword[i % len(keyword)]) - 65
        enc2 += chr((ord(ch) - 65 + shift) % 26 + 65)
        i += 1
    else:
        enc2 += ch

dec2 = ""
i = 0
for ch in enc2:
    if ch.isalpha():
        shift = ord(keyword[i % len(keyword)]) - 65
        dec2 += chr((ord(ch) - 65 - shift) % 26 + 65)
        i += 1
    else:
        dec2 += ch

print("\n-- Vigenere (Polyalphabetic) Cipher --")
print("Keyword   :", keyword)
print("Original  :", text2)
print("Encrypted :", enc2)
print("Decrypted :", dec2)