from cryptography.fernet import Fernet

message = "The femboys are coming"
key = Fernet.generate_key()
fernet = Fernet(key)
encMessage = fernet.encrypt(message.encode())
print("original string: ", message)
print("encrypted string: ", encMessage.decode("utf-8"))
decMessage = fernet.decrypt(encMessage).decode()
print("decrypted string: ", decMessage)
