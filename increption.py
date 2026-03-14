# RC4 Encryption and Decryption

def rc4(key, text):
    S = list(range(256))
    j = 0
    out = []

    # Key Scheduling Algorithm (KSA)
    for i in range(256):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        S[i], S[j] = S[j], S[i]

    # Pseudo Random Generation Algorithm (PRGA)
    i = j = 0
    for char in text:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        out.append(chr(ord(char) ^ k))

    return ''.join(out)


key = "secretkey"
password = "mypassword"

# Encryption
encrypted = rc4(key, password)
print("Encrypted Password:", encrypted)

# Decryption
decrypted = rc4(key, encrypted)
print("Decrypted Password:", decrypted)