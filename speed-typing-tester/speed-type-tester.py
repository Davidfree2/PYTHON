import time
import random
from colorama import Fore

def create_dictonary():
    import_dictionary_file = open('dictionary.txt')    
    read_dictionary_file  = import_dictionary_file.read()   
    split_dictionary_file_to_list = read_dictionary_file.split()
    randomized_dictionary_spliced = random.sample(split_dictionary_file_to_list, 20)
    convert_dic_to_string = ' '.join(randomized_dictionary_spliced)
    return convert_dic_to_string

def start_game(): 
    user_start_game = input('would you like to start the game?')
    if user_start_game == 'yes':
        words = create_dictonary()
        print(words)
        go = input('')
        while go != words:
            print(Fore.RED + 'try again!')
            print(Fore.WHITE + words)
            go = input('')
        else:
            print(Fore.BLUE + 'You did it!')
    else:
        print('maybe next time!')


def count_time():
    current_time = time.time()
    return round(current_time)


def calculate_entire_time(start_time, end_time):
    calcultated_time = end_time - start_time
    return calcultated_time


start_time = count_time()
start_game()
end_time = count_time()
print(f'{calculate_entire_time(start_time, end_time)} seconds')

