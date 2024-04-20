from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

def load_private_key(private_key_path):

# Path to your private key file (replace with the actual path)
    private_key_path = "private_key.pem"

    # Password (optional)
    password = b"prashant"  # Set a password if your key is encrypted

    try:
        with open(private_key_path, "rb") as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=password,
                backend=default_backend()
            )
    except ValueError as e:
        print(f"Error loading private key: {e}")
    # Handle the error (e.g., prompt user for password if the key is encrypted)

    return private_key

load_private_key("private_key.pem")