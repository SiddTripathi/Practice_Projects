import random

def guess(x):
    random_num =  str(random.randint(1,x))
    guess =0
    while guess != random_num:
        guess = input(f'Guess the number between 1 and{x}:')
        if(guess< random_num and guess!=''):
            print('Guess again. Its low')
        elif(guess>random_num and guess!=''):
            print('Sorry Number too high ')
        elif(guess==''):
            print('No value detected. Please enter a value')
            
    
    print('You got the right guess ! Well done')


guess(10)