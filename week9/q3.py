import hmac
import hashlib

def generate_hmac(message, secret_key):
    # Use SHA-256 as the hash function
    hmac_object = hmac.new(secret_key.encode('utf-8'), message.encode('utf-8'), hashlib.sha256)
    return hmac_object.hexdigest()

message = "This is a secret message."
secret_key = "my_secret_key"

hmac_value = generate_hmac(message, secret_key)
print("Generated HMAC:", hmac_value)

def verify_hmac(message, secret_key, hmac_value):
    # Generate HMAC for the message
    new_hmac = generate_hmac(message, secret_key)
    return hmac.compare_digest(new_hmac, hmac_value)


is_valid = verify_hmac(message, secret_key, hmac_value)
print("Is the HMAC valid?", is_valid)
