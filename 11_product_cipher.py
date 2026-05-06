# Practical 11 - Product Cipher (Caesar + Rail Fence combined)

text  = input("Enter text: ").upper().replace(" ", "")
shift = int(input("Enter Caesar shift: "))
rails = int(input("Enter Rail Fence rails: "))

# Step 1: Caesar Encrypt
step1 = ""
for ch in text:
    if ch.isalpha():
        step1 += chr((ord(ch) - 65 + shift) % 26 + 65)
    else:
        step1 += ch

# Step 2: Rail Fence Encrypt
fence = [[] for _ in range(rails)]
rail = 0
direction = 1
for ch in step1:
    fence[rail].append(ch)
    if rail == 0:
        direction = 1
    elif rail == rails - 1:
        direction = -1
    rail += direction

encrypted = ''.join(''.join(row) for row in fence)

print("\n-- Encryption --")
print("Original         :", text)
print("After Caesar     :", step1)
print("After Rail Fence :", encrypted)

# --- Decryption ---

# Step 1: Rail Fence Decrypt
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

step3 = ''.join(plain)

# Step 2: Caesar Decrypt
decrypted = ""
for ch in step3:
    if ch.isalpha():
        decrypted += chr((ord(ch) - 65 - shift) % 26 + 65)
    else:
        decrypted += ch

print("\n-- Decryption --")
print("After Rail Fence:", step3)
print("After Caesar   :", decrypted)