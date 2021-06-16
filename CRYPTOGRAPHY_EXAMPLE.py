#https://cryptography.io/en/latest/fernet/
from cryptography.fernet import Fernet




key = Fernet.generate_key()

print(key)

message = "hello universe and world ".encode()

f = Fernet(key)

encrypted = f.encrypt(message)

print(encrypted)

decrypted_encrypted = f.decrypt(encrypted)
print(decrypted_encrypted)