# ROCK, PAPER, SCISSOR GAME
import random

def rock_outcomes():
     if user_guess == 'rock' and random_things == 'rock':
        print(f'\nDraw!\n')
        print(f'\ntry again!\n')
        
     elif user_guess == 'rock' and random_things == 'scissors':
        print(f'\nYou win!\n')
        print(f'hit play again to start again!')
        deadman = False
        
     elif user_guess == 'rock' and random_things == 'paper':
        print(f'\nYou lose!\n')
        print(f'\nhit play again to start again!\n')
        deadman = False

possible_things = ['rock', 'paper', 'scissors']
random_things = random.choice(possible_things)



game_start_prompt = input('hello this is a rock, paper, scissors game would you like to start? type yes to start or no to exit')

deadman = ''
if game_start_prompt == 'yes':
    deadman = True
else:
    deadman = False
    
print(random_things)

while deadman == True:
    user_guess = input('pick rock, paper, or scissors')
    
    rock_outcomes()
    
    if user_guess == 'paper' and random_things == 'paper':
        print(f'\nDraw!\n')
        print(f'\ntry again!\n')
        
    elif user_guess == 'paper' and random_things == 'rock':
        print(f'\nYou win!\n')
        print(f'hit play again to start again!')
        deadman = False
        
    elif user_guess == 'paper' and random_things == 'scissors':
        print(f'\nYou lose!\n')
        print(f'\nhit play again to start again!\n')
        deadman = False
        
    elif user_guess == 'scissors' and random_things == 'scissors':
        print(f'\nDraw!\n')
        print(f'\ntry again!\n')
        
    elif user_guess == 'scissors' and random_things == 'paper':
        print(f'\nYou win!\n')
        print(f'hit play again to start again!')
        deadman = False
        
    elif user_guess == 'scissors' and random_things == 'rock':
        print(f'\nYou lose!\n')
        print(f'\nhit play again to start again!\n')
        deadman = False
        
        
    