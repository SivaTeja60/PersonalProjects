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
def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback!='c':
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f'is {guess} too high(H), too low(L), or correct(C)').lower()
        if feedback == 'h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
    print(f'The computer guessed number {guess} is correct')
    
computer_guess(10)