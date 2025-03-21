def caesar_encrypt(plaintext, shift):
    return ''.join([chr((ord(c) + shift - 65) % 26 + 65) if c.isupper() else
                    chr((ord(c) + shift - 97) % 26 + 97) if c.islower() else c for c in plaintext])

def caesar_decrypt(ciphertext, shift):
    return ''.join([chr((ord(c) - shift - 65) % 26 + 65) if c.isupper() else
                    chr((ord(c) - shift - 97) % 26 + 97) if c.islower() else c for c in ciphertext])

plaintext = "Hello, World!"
shift = 3

encrypted_text = caesar_encrypt(plaintext, shift)
print(f"Encrypted Text: {encrypted_text}")

decrypted_text = caesar_decrypt(encrypted_text, shift)
print(f"Decrypted Text: {decrypted_text}")
