import random
print("Welcome to Guess the Number Game :")

def guess_number(x):
    guess = 0
    random_num = random.randint(1,x)
    while guess != random_num:
        guess = int(input(f"Enter number between 1 to {x}:"))
        if guess == random_num:
            print(f" Yay Congrats , You have guessed the number {random_num} correctly")
        elif guess < random_num:
            print(f"Sorry guess again , Too Low")
        else:
            print(f"Sorry guess again , Too High")


guess_number(20)
