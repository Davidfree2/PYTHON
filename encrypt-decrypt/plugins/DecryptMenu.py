import plugins.Banner
import plugins.Menu
from cryptography.fernet import Fernet



class Decrypt_Menu:
    def __init__(self):
        pass

    def DecryptMenu(self):
        print('----------------------------------------------------------------------------------------------------------------\n\n')
        plugins.Banner.Logo().BannerDecrypt()
        key = input('what is the key(feel free to copy and paste it here)\n')
        #object key turns the key into a simple object for use
        object_key = Fernet(key)
        encrypted_source = input('what is the encrypted message?\n')
        decrypted = object_key.decrypt(bytes(encrypted_source, 'utf-8'))
        print('\nDecrypted:')
        print(f'{decrypted.decode("utf-8")}\n')
        wait = input('press enter to continue')
        plugins.Menu.Menu().menu()



