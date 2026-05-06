# Practical 7 - Playfair Cipher

key = input("Enter key: ").upper().replace("J", "I")
text = input("Enter text: ").upper().replace("J", "I")

# Build 5x5 matrix
seen = []
for ch in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
    if ch not in seen:
        seen.append(ch)
matrix = [seen[i*5:(i+1)*5] for i in range(5)]

print("\nPlayfair Matrix:")
for row in matrix:
    print(' '.join(row))

# Prepare digraphs
text = ''.join(c for c in text if c.isalpha())
pairs = []
i = 0
while i < len(text):
    a = text[i]
    b = text[i+1] if i+1 < len(text) else 'X'
    if a == b:
        pairs.append((a, 'X'))
        i += 1
    else:
        pairs.append((a, b))
        i += 2

# Find position in matrix
def pos(ch):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == ch:
                return r, c

# Encrypt
encrypted = ""
for a, b in pairs:
    ra, ca = pos(a)
    rb, cb = pos(b)
    if ra == rb:
        encrypted += matrix[ra][(ca+1)%5] + matrix[rb][(cb+1)%5]
    elif ca == cb:
        encrypted += matrix[(ra+1)%5][ca] + matrix[(rb+1)%5][cb]
    else:
        encrypted += matrix[ra][cb] + matrix[rb][ca]

# Decrypt
decrypted = ""
enc_pairs = [(encrypted[i], encrypted[i+1]) for i in range(0, len(encrypted), 2)]
for a, b in enc_pairs:
    ra, ca = pos(a)
    rb, cb = pos(b)
    if ra == rb:
        decrypted += matrix[ra][(ca-1)%5] + matrix[rb][(cb-1)%5]
    elif ca == cb:
        decrypted += matrix[(ra-1)%5][ca] + matrix[(rb-1)%5][cb]
    else:
        decrypted += matrix[ra][cb] + matrix[rb][ca]

print("\nOriginal  :", text)
print("Encrypted :", encrypted)
print("Decrypted :", decrypted)