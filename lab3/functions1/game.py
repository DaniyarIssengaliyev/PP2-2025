import random

def guess_the_number(name):
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number_to_guess = random.randint(1,20)
    attempts = 0
    while True:
        print("Take a guess.")
        num = int(input(""))
        attempts += 1
        if num < number_to_guess:
            print("Your guess is too low.")
        elif num > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break
name = input("Hello! What is your name?: ")
guess_the_number(name)