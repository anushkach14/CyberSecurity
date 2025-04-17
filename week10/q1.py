from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# 1. Creates a public-private RSA key pai
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# 2. Message to sign
message = b"Hello, this is a signed message!"

# 3. Signs a message using the private key.
signature = private_key.sign(
    message,
    padding.PKCS1v15(),
    hashes.SHA256()
)

# 4. Verifies the signature using the public key
try:
    public_key.verify(
        signature,
        message,
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    print(" Signature is valid.")
except:
    print(" Signature is invalid.")
