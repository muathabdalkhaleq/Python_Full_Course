# python number guessing game
import random
low_num = 1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0

is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {low_num} and {high_num}")

while is_running:
    guess = input("Enter Your Guess :")

    if guess.isdigit():
        guess = int(guess)
        guesses+=1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
            print(f"Please Select a number between {low_num} and {high_num}")
        elif guess > answer:
            print("Too high")
        elif guess < answer:
            print("Too low")
        else:
            print(f"That was the CORRECT answer! ==>{answer} after {guesses} guesses")
            is_running = False
        
    else:
        print("Invalid Guess")
        print(f"Please Select a number between {low_num} and {high_num}")

