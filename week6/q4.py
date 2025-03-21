import numpy as np

def create_key_matrix(key):
    return np.array([[ord(key[0]) - 65, ord(key[1]) - 65],
                     [ord(key[2]) - 65, ord(key[3]) - 65]])

def encrypt(plaintext, key):
    matrix = create_key_matrix(key)
    # Convert letters to numbers and encrypt using matrix multiplication
    pt_numbers = [ord(plaintext[0]) - 65, ord(plaintext[1]) - 65]
    cipher_numbers = np.dot(matrix, pt_numbers) % 26
    # Convert back to letters
    return chr(cipher_numbers[0] + 65) + chr(cipher_numbers[1] + 65)

def decrypt(ciphertext, key):
    matrix = create_key_matrix(key)
    # Find inverse of the key matrix
    det = int(np.round(np.linalg.det(matrix)))
    inv_matrix = np.linalg.inv(matrix) * det
    inv_matrix = np.round(inv_matrix).astype(int) % 26
    # Convert ciphertext to numbers and decrypt using inverse matrix
    ct_numbers = [ord(ciphertext[0]) - 65, ord(ciphertext[1]) - 65]
    pt_numbers = np.dot(inv_matrix, ct_numbers) % 26
    # Convert back to letters
    return chr(pt_numbers[0] + 65) + chr(pt_numbers[1] + 65)

key = "GYBN"  # 2x2 matrix key (4 characters)
plaintext = "HI"

ciphertext = encrypt(plaintext, key)
print("Encrypted:", ciphertext)

decrypted_text = decrypt(ciphertext, key)
print("Decrypted:", decrypted_text)
