import hashlib

def md5_hash(message):
    md5 = hashlib.md5()  # Create an MD5 hash object
    md5.update(message.encode('utf-8'))  # Encode message to bytes and update the hash object
    return md5.hexdigest()  # Returns the hash as a hexadecimal string

message = "Hello, this is a test message."

print("MD5 Hash:", md5_hash(message))
