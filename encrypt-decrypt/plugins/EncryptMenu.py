import plugins.Banner
import random
import plugins.Menu
from cryptography.fernet import Fernet


class Encrypt_Menu:
    def __init__(self):
        pass
    
    def EncryptMenu(self):
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','f','w','x','y','z']
        numbers = [1,2,3,4,5,6,7,8,9]
        specialChars = ['!','@','#','%','&','*','?','.',',','/',':',';']
        combinedEverything = letters + numbers + specialChars
        randomized_password = []
        randomized_string = ''

        print('----------------------------------------------------------------------------------------------------------------\n\n')
        plugins.Banner.Logo().BannerEncrypt()
        
     
        print('''
                [0] Generate Password And Encrypt
                [1] Encrypt Message
                [9] Go Back
                ''')
        user_input = int(input('What would you like to do?'))
        
        if user_input == 0:
            generate_key = Fernet.generate_key()
            objectKey = Fernet(generate_key)
            for i in range(24):
                randomized_password.append(random.choice(combinedEverything))
        
            for i in randomized_password:
                randomized_string += str(i)
        
            print(f'\nYour Password: \n{randomized_string}\n')
            encrypted_password = objectKey.encrypt(bytes(randomized_string, 'utf-8'))
            print(f'Your Encryped Password: {encrypted_password.decode("utf-8")}')
            print(f'\nYour Key: {generate_key.decode("utf-8")}')
            wait = input('press enter to continue')
            plugins.Menu.Menu().menu()
        elif user_input == 1:
            user_message = input('type the message you would like to encrypt\n')
            generate_key = Fernet.generate_key()
            objectKey = Fernet(generate_key)
            print(f'\nYour Message: \n{user_message}\n')
            Encrypted_Message= objectKey.encrypt(bytes(user_message, 'utf-8'))
            print(f'Your Encryped Message: {Encrypted_Message.decode("utf-8")}')
            print(f'\nYour Key: {generate_key.decode("utf-8")}')
            wait = input('press enter to continue')
            plugins.Menu.Menu().menu()
        elif user_input == 9:
            plugins.Menu.Menu().menu()
        else: 
            print('Choose something or press <control + C> to exit')
            Encrypt_Menu().EncryptMenu()






