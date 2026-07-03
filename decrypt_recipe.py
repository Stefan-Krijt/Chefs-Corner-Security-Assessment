import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# The encrypted content from the API response
encrypted_content = "gAAAAABqRQKzZn73KJ3vQHs6AsA5FZK9lSU9bEgDMMYEcW1oCfyJDoUdwcCnL1l17XtW7XXv2ORdgip2qHKIDxsOUF88IRVv864yX3ypvfwOuCADpFVTSC_qOWFgvZ1pTTLbJjtLVTTnFVrE2VoJfGfe6Djbd0M9gZD1hLp98Mkc3KsK5GBFopel8kM665bCeANrNIvyY1EUL9eqaKTB94NlrxYCQwvN9XuszfwwoLmI_0_JUAvANos="

# The encryption key from the commit history
encryption_key = "weak-encryption-key-789"

# Fixed salt from app.py
salt = b'chefs_corner_salt'

# Derive the key using PBKDF2 (same as server)
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
)
derived_key = base64.urlsafe_b64encode(kdf.derive(encryption_key.encode()))
fernet = Fernet(derived_key)

# Decrypt the content
try:
    decrypted = fernet.decrypt(encrypted_content.encode()).decode()
    print("=" * 60)
    print("SECRET RECIPE DECRYPTED!")
    print("=" * 60)
    print(decrypted)
    print("=" * 60)
except Exception as e:
    print(f"Decryption failed: {e}")
