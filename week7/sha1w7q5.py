import hashlib

def sha1_hash(text):
    return hashlib.sha1(text.encode()).hexdigest()

msg="hello hacker"
hash_value=sha1_hash(msg)

print(f"message : {msg}")
print(f"SHA-1 Hash : {hash_value}")
