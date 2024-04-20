# Extract the public key from the private key object (this is the public key derivation)
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

import loadprivatekey

private_key = loadprivatekey.load_private_key("private_key.pem")

public_key = private_key.public_key()

# Optional: Write the keys to separate PEM files
with open("public_key.pem", "wb") as f:
    f.write(
        public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    )

print("Public Key retrieved successfully!")