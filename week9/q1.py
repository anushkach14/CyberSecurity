import hashlib

def sha1_hash(message):
    sha1 = hashlib.sha1()
    sha1.update(message.encode('utf-8'))  # Encoding message to bytes
    return sha1.hexdigest() 


def sha256_hash(message):
    sha256 = hashlib.sha256()
    sha256.update(message.encode('utf-8'))  
    return sha256.hexdigest()  # Returns the hash as a hexadecimal string

def sha3_256_hash(message):
    sha3_256 = hashlib.sha3_256()
    sha3_256.update(message.encode('utf-8'))  
    return sha3_256.hexdigest()  

message = "Hello, this is a test message."

print("SHA-1 Hash:", sha1_hash(message))
print("SHA-256 Hash:", sha256_hash(message))
print("SHA3-256 Hash:", sha3_256_hash(message))
