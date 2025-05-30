import random
class SimpleBlowfish:
    def __init__(self, key):
        random.seed(sum(bytearray(key.encode()))) 
        self.key = [random.randint(0, 255) for _ in range(16)]  
    def encrypt(self, plaintext):
        encrypted = [chr(ord(c) ^ self.key[i % len(self.key)]) for i, c in enumerate(plaintext)]
        return "".join(encrypted)

    def decrypt(self, ciphertext):
        decrypted = [chr(ord(c) ^ self.key[i % len(self.key)]) for i, c in enumerate(ciphertext)]
        return "".join(decrypted)
key = input("Enter a secret key: ")
plaintext = input("Enter text to encrypt: ")
cipher = SimpleBlowfish(key)
ciphertext = cipher.encrypt(plaintext)
print("Encrypted:", ciphertext)
decrypted_text = cipher.decrypt(ciphertext)
print("Decrypted:", decrypted_text)
