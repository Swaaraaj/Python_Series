import random
print(f"Welcome to Guess the number with Computer")

def guess_num_comp(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess_num = random.randint(low,high)
        else:
            guess_num = low
        feedback = (input(f'Is {guess_num} too High [H] , too Low [L] , Correct [C] :'))
        if feedback == "h" or feedback == "H":
            high = guess_num - 1
        elif feedback == "l" or feedback == "L":
            low = guess_num + 1

    print(f"Yay! The Compute guessed the number , {guess_num} correctly")

guess_num_comp(10)