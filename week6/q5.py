import numpy as np

def feistel_round(left, right, key):
    round_result = left ^ (right ^ key)
    return round_result, right

def encrypt(plaintext, key, rounds=2):
    left = (plaintext >> 4) & 0xF
    right = plaintext & 0xF

    for _ in range(rounds):
        left, right = feistel_round(left, right, key)   # Combine the two halves back into one block

    return (left << 4) | right

def decrypt(ciphertext, key, rounds=2):
    left = (ciphertext >> 4) & 0xF
    right = ciphertext & 0xF

    for _ in range(rounds):
        left, right = feistel_round(left, right, key)

    return (left << 4) | right

plaintext = 0b101011
key = 0b0110

print(f"Original plaintext (6 bits): {bin(plaintext)}")
ciphertext = encrypt(plaintext, key, rounds=2)
print(f"Ciphertext (after encryption): {bin(ciphertext)}")

decrypted_text = decrypt(ciphertext, key, rounds=2)
print(f"Decrypted text (back to plaintext): {bin(decrypted_text)}")
