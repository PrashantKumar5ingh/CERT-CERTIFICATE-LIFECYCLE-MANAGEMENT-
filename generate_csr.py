from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

import loadprivatekey

key = loadprivatekey.load_private_key("private_key.pem")
# Generate a CSR
csr = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
    # Provide various details about who we are.
    x509.NameAttribute(NameOID.COUNTRY_NAME, "IN"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "Chennai"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, "Avadi"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "My Company"),
    x509.NameAttribute(NameOID.COMMON_NAME, "mysite.com"),
])).add_extension(
    x509.SubjectAlternativeName([
        # Describe what sites we want this certificate for.
        x509.DNSName("mysite.com"),
        x509.DNSName("mysite.in"),
        x509.DNSName("subdomain.mysite.com"),
    ]),
    critical=False,
# Sign the CSR with our private key.
).sign(key, hashes.SHA256())
# Write our CSR out to disk.
with open("csr.pem", "wb") as f:
    f.write(csr.public_bytes(serialization.Encoding.PEM))

print("CSR is Generated!")