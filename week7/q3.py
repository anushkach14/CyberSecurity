import random  # Import the random module to generate random numbers

class SimpleTwofish:  # Define the SimpleTwofish class
    def __init__(self, key):  # The constructor method that accepts a key as input
        self.key = self.expand_key(key)  # Calls the expand_key method to initialize the key

    def expand_key(self, key):  # Method to expand and convert the key into a list of numbers
        random.seed(sum(bytearray(key.encode())))  # Seed the random number generator using the key's byte sum
        return [random.randint(0, 255) for _ in range(16)]  # Generate 16 random integers between 0 and 255
    
    def encrypt(self, plaintext):  # Method to encrypt plaintext using XOR with the expanded key
        encrypted = [chr(ord(c) ^ self.key[i % len(self.key)]) for i, c in enumerate(plaintext)]  # XOR encryption
        return "".join(encrypted)  # Return the encrypted text as a string
    
    def decrypt(self, ciphertext):  # Method to decrypt ciphertext by reversing the XOR operation
        decrypted = [chr(ord(c) ^ self.key[i % len(self.key)]) for i, c in enumerate(ciphertext)]  # XOR decryption
        return "".join(decrypted)  # Return the decrypted text as a string

key = input("Enter a secret key (8-16 characters): ")
plaintext = input("Enter text to encrypt: ")
cipher = SimpleTwofish(key)
ciphertext = cipher.encrypt(plaintext)
print("Encrypted:", ciphertext)

decrypted_text = cipher.decrypt(ciphertext)
print("Decrypted:", decrypted_text)
