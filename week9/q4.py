import hmac
import hashlib
import rsa

# HMAC Implementation
def generate_hmac(message, secret_key):
    return hmac.new(secret_key.encode('utf-8'), message.encode('utf-8'), hashlib.sha256).hexdigest()

def verify_hmac(message, secret_key, hmac_value):
    return hmac.compare_digest(generate_hmac(message, secret_key), hmac_value)

# RSA Digital Signature Implementation
def generate_rsa_keys():
    return rsa.newkeys(512)  # Generate public/private RSA keys

def sign_message(message, private_key):
    return rsa.sign(message.encode('utf-8'), private_key, 'SHA-256')

def verify_signature(message, signature, public_key):
    try:
        rsa.verify(message.encode('utf-8'), signature, public_key)
        return True
    except rsa.VerificationError:
        return False

# Test Messages
message = "This is a test message."
secret_key = "supersecretkey"

# 1. HMAC Example
hmac_value = generate_hmac(message, secret_key)
print("Generated HMAC:", hmac_value)
print("Is HMAC valid?", verify_hmac(message, secret_key, hmac_value))

# 2. Digital Signature Example
public_key, private_key = generate_rsa_keys()
signature = sign_message(message, private_key)
print("Generated Digital Signature:", signature)
print("Is the digital signature valid?", verify_signature(message, signature, public_key))
