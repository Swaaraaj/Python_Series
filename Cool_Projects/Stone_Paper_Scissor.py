import random

def play():
    user = input(f" What's Your Choice ?'r' for rock , 'p' for paper , 's' for scissors \n Your Hand:")
    computer = random.choice(['r','p','s'])

    print("Computer Hand:")
    if computer == 'r':
        print("Rock")
    elif computer == 'p':
        print("Paper")
    else:
        print("Scissor")



    if user == computer:
        return "Tie"

    if is_win(user,computer):
        return "You Won!"
    return "you Lost!"


def is_win(player,opppenent):

    # r>s , s>p , p>r
    if(player == 'r' and opppenent == 's' )or (player == 's' and opppenent == 'p') or (player == 'p' and opppenent == 'r'):
        return True


print(play())