import base64
import hashlib
from cryptography.fernet import Fernet


def gen_fernet_key(passcode: bytes) -> bytes:
    assert isinstance(passcode, bytes)
    hlib = hashlib.md5()
    hlib.update(passcode)
    return base64.urlsafe_b64encode(hlib.hexdigest().encode('latin-1'))


password = 'hello'
key = gen_fernet_key(password.encode('utf-8'))
fernet = Fernet(key)
data_in = "the british are coming"
cypher_text = fernet.encrypt(data_in.encode('utf-8'))
decr_data = fernet.decrypt(cypher_text).decode('utf-8')


print(f"cypher_text: {cypher_text}")

