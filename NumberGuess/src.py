import random

def guess(num):
    random_number=random.randint(1,num)
    guess=0
    while guess!=random_number:
        guess=int(input(f"Guess a number between 1 and {num} "))
        if guess<random_number:
            print("sorry guess is too low")
        elif guess>random_number:
            print("sorry guess is too high")
    print(f"Congrats your guess {random_number} is correct")

guess(10)