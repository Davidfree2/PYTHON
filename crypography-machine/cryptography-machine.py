from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)


message = input('what message would you like to encrypt?\nMessage:').encode()
print('\n')

print(f'this is your key(youll use this to decrypte your message)\nKey:{key}')

encrypted_message = f.encrypt(message)

print('\n')
print(f'---------------------\nthis is your encrypted message\nENCRYPTED MESSAGE: {encrypted_message}')

print('\n')
decrypted_message= f.decrypt(encrypted_message)

print(f'---------------------\nthis is your decrypted message using your key\nDECRYPTED MESSAGE: {decrypted_message}')
