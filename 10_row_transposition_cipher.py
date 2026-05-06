# Practical 10 - Row Transposition Cipher

text = input("Enter text: ").upper().replace(" ", "")
key  = input("Enter key (e.g. 3142): ")

num_cols = len(key)
# Pad text with X
while len(text) % num_cols != 0:
    text += 'X'

num_rows = len(text) // num_cols

# Fill grid row by row
grid = []
for i in range(num_rows):
    grid.append(list(text[i*num_cols:(i+1)*num_cols]))

print("\nGrid:")
print("Key :", ' '.join(key))
for row in grid:
    print('    ', ' '.join(row))

# Read columns in key order (ascending)
order = sorted(range(num_cols), key=lambda x: key[x])

encrypted = ""
for col in order:
    for row in grid:
        encrypted += row[col]

# Decrypt
cols = {}
idx = 0
for col in order:
    cols[col] = list(encrypted[idx:idx+num_rows])
    idx += num_rows

decrypted = ""
for r in range(num_rows):
    for c in range(num_cols):
        decrypted += cols[c][r]

decrypted = decrypted.rstrip('X')

print("Original  :", text)
print("Encrypted :", encrypted)
print("Decrypted :", decrypted)