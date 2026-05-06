# Practical 8 - Hill Cipher (2x2 key matrix)

text = input("Enter text (even number of letters): ").upper()
text = ''.join(c for c in text if c.isalpha())
if len(text) % 2 != 0:
    text += 'X'

# Key matrix [[3,3],[2,5]] - determinant = 9, inverse mod 26 exists
key = [[3, 3], [2, 5]]

print("Key Matrix:")
print(key[0])
print(key[1])

# Encrypt
encrypted = ""
for i in range(0, len(text), 2):
    a = ord(text[i]) - 65
    b = ord(text[i+1]) - 65
    c1 = (key[0][0]*a + key[0][1]*b) % 26
    c2 = (key[1][0]*a + key[1][1]*b) % 26
    encrypted += chr(c1+65) + chr(c2+65)

# Inverse key matrix mod 26

inv_key = [[(5*3)%26, ((-3)*3)%26], [((-2)*3)%26, (3*3)%26]]

# Decrypt
decrypted = ""
for i in range(0, len(encrypted), 2):
    a = ord(encrypted[i]) - 65
    b = ord(encrypted[i+1]) - 65
    p1 = (inv_key[0][0]*a + inv_key[0][1]*b) % 26
    p2 = (inv_key[1][0]*a + inv_key[1][1]*b) % 26
    decrypted += chr(p1+65) + chr(p2+65)

print("Original  :", text)
print("Encrypted :", encrypted)
print("Decrypted :", decrypted)