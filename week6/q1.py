def xor_encrypt_decrypt(plaintext, key):
    return ''.join(chr(ord(c) ^ key) for c in plaintext)

plaintext = "Cyber Security"

keys = [0, 1, 5]

for key in keys:
    encrypted_text = xor_encrypt_decrypt(plaintext, key)
    print(f"Encrypted (key={key}): {encrypted_text}")
    
    decrypted_text = xor_encrypt_decrypt(encrypted_text, key)
    print(f"Decrypted (key={key}): {decrypted_text}")

