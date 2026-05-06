
text = input("Enter text: ").upper()
shift = int(input("Enter shift: "))
 
encrypted = ""
for ch in text:
    if ch.isalpha():
        encrypted += chr((ord(ch) - 65 + shift) % 26 + 65)
    else:
        encrypted += ch
 
decrypted = ""
for ch in encrypted:
    if ch.isalpha():
        decrypted += chr((ord(ch) - 65 - shift) % 26 + 65)
    else:
        decrypted += ch
 
print("Original  :", text)
print("Encrypted :", encrypted)
print("Decrypted :", decrypted)
 