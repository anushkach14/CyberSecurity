def generate_matrix(key):
    key = ''.join(sorted(set(key), key=lambda x: key.index(x))).replace('J', 'I')
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = ''.join([c for c in key + alphabet if c not in key])
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(char, matrix):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)

def preprocess_text(text):
    text = text.upper().replace('J', 'I')
    result = ""
    for i in range(0, len(text), 2):
        if i+1 < len(text) and text[i] == text[i+1]:
            result += text[i] + 'X'
        else:
            result += text[i:i+2]
    return result

def playfair(text, key, encrypt=True):
    matrix = generate_matrix(key)
    text = preprocess_text(text)
    result = ''
    for i in range(0, len(text), 2):
        char1, char2 = text[i], text[i+1]
        row1, col1 = find_position(char1, matrix)
        row2, col2 = find_position(char2, matrix)
        if row1 == row2: result += matrix[row1][(col1 + (1 if encrypt else -1)) % 5] + matrix[row2][(col2 + (1 if encrypt else -1)) % 5]
        elif col1 == col2: result += matrix[(row1 + (1 if encrypt else -1)) % 5][col1] + matrix[(row2 + (1 if encrypt else -1)) % 5][col2]
        else: result += matrix[row1][col2] + matrix[row2][col1]
    return result

# Example usage
key = "KEYWORD"
plaintext = "HELLO PLAYFAIR"
ciphertext = playfair(plaintext, key, encrypt=True)
print(f"Encrypted: {ciphertext}")
decrypted_text = playfair(ciphertext, key, encrypt=False)
print(f"Decrypted: {decrypted_text}")
