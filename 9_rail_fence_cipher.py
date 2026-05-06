# Practical 9 - Rail Fence Cipher

text = input("Enter text: ").replace(" ", "")
rails = int(input("Enter number of rails: "))

# Encrypt
fence = [[] for _ in range(rails)]
rail = 0
direction = 1

for ch in text:
    fence[rail].append(ch)
    if rail == 0:
        direction = 1
    elif rail == rails - 1:
        direction = -1
    rail += direction

encrypted = ''.join(''.join(row) for row in fence)

# Show rail pattern
print("\nRail pattern:")
for i, row in enumerate(fence):
    print(f"Rail {i}: {''.join(row)}")

# Decrypt
n = len(encrypted)
pattern = []
rail = 0
direction = 1
for _ in range(n):
    pattern.append(rail)
    if rail == 0:
        direction = 1
    elif rail == rails - 1:
        direction = -1
    rail += direction

counts = [pattern.count(r) for r in range(rails)]
segments = []
idx = 0
for count in counts:
    segments.append(list(encrypted[idx:idx+count]))
    idx += count

plain = []
rail_idx = [0] * rails
for r in pattern:
    plain.append(segments[r][rail_idx[r]])
    rail_idx[r] += 1

decrypted = ''.join(plain)

print("Original  :", text)
print("Encrypted :", encrypted)
print("Decrypted :", decrypted)