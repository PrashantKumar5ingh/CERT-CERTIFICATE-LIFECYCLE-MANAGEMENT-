from cryptography import x509

# Path to your CSR file (replace with the actual path)

def load_csr(csr_path="csr.pem"):
    try:
        # Open the CSR file in read mode
        with open(csr_path, "rb") as csr_file:
            csr_data = csr_file.read()

    # Load the CSR data as a cryptography.x509.CertificateSigningRequest object

    # Use the public key object (e.g., for verification)
    # ... (your code to use the public key)

    except FileNotFoundError as e:
        print(f"Error: CSR file not found ({csr_path})")
    except ValueError as e:
        print(f"Error loading CSR: {e}")
    

    loaded_csr = x509.load_pem_x509_csr(bytes(csr_data))
    return loaded_csr