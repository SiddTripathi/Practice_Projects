import random
def comp_guess(x):
    low=1
    high =x
    feedback = ''
    while feedback !='c':
        if low!=high:
           guess = random.randint(low,high)
        else:
            guess=low
        feedback = input(f'Is {guess} too - High (H), Low(L), Correct(C)').lower()
        if feedback =='h':
            high=guess-1
        elif feedback =='l':
            low=guess+1
    
    print('Yay ! Computer Guessed your number correctly')
        
        




comp_guess(10)