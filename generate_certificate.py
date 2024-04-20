from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import datetime
import loadprivatekey
import loadcsr

csr = loadcsr.load_csr("csr.pem")
key = loadprivatekey.load_private_key("private_key.pem")
subject = csr.subject
issuer = subject
cert = x509.CertificateBuilder().subject_name(
    subject
).issuer_name(
    issuer
).public_key(
    key.public_key()
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    datetime.datetime.now(datetime.timezone.utc)
).not_valid_after(
    # Our certificate will be valid for 10 days
    datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=10)
).add_extension(
    x509.SubjectAlternativeName([x509.DNSName("localhost")]),
    critical=False,
# Sign our certificate with our private key
).sign(key, hashes.SHA256())
# Write our certificate out to disk.
with open("certificate.crt", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

print("Certificate is Generated!")