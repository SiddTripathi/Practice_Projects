import random

def game():
    user = input("Please enter your choice from - 'r' - Rock, 'p'- Paper, 's' - Scissor   ")
    comp = random.choice(['r','p','s'])
    print(comp)
    print(user)

    if user == comp:
        return 'It\'s a tie'
    
    elif is_win(user, comp):
        return 'You Won'

    return 'You have lost'


def is_win(hooman,computer):
    if(hooman=='r' and computer=='s') or (hooman=='p' and computer=='r') or (hooman=='s' and computer=='p'):
        return True

print(game())