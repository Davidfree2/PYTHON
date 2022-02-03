import plugins.EncryptMenu
import plugins.DecryptMenu
import plugins.Banner


class Menu:
    def __init__(self):
        pass

    def menu(self):
        print('----------------------------------------------------------------------------------------------------------------\n\n')
        plugins.Banner.Logo().BannerEncrypt()
        plugins.Banner.Logo().BannerLineSpace()
        plugins.Banner.Logo().BannerDecrypt()
        plugins.Banner.Logo().Creator()
        print('''
        ----------------------------------------------------
        [0] Encrypt - Create Encrypted Messages/Password
        [1] Decrypt - Decrypt Created Messages/Password (requires key)
        ----------------------------------------------------''')
        Choose_path = int(input('        What would you like to do?'))
        if Choose_path == 0:
            plugins.EncryptMenu.Encrypt_Menu().EncryptMenu()
        elif Choose_path == 1:
            plugins.DecryptMenu.Decrypt_Menu().DecryptMenu()
        else: 
            print('Choose something or press <control + C> to exit')
            Menu().menu()
        

