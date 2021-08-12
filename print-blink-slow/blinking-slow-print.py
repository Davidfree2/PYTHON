import time

unicode_char = "\u2588"
string = input('what would you like to print our?')

splited_string = ''.join(string) 

for single in splited_string:
    print(single, end='', flush= True)
    time.sleep(.04)

print('')

for single in range(3):
    print(unicode_char , end='\r', flush= True)
    time.sleep(.55)
    print(' ', end='\r', flush= True)
    time.sleep(.55)










