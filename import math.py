import random
import time

secret_number = random.randint(1,10)
attempts = 0
while True:
    guess_number = int(input("enter you number: "))
    attempts += 1
    if secret_number != guess_number:
        print("Wrong answer, try again")
    if secret_number == guess_number:
        print("Congratulstions, you guessed hidden number!")
        print("Total attempts number =", attempts)
    if guess_number < secret_number:
        print("Hint: Hidden number is bigger than your number")
        print("attempts number =", attempts)
    if guess_number > secret_number:
        print("Hint: Hidden number is smaller than your number")
        print("attempts number =", attempts)
    if attempts == 3:
        print("you're stupid, wait 5 seconds...")
        attempts = 0
        time.sleep(5)
        print("Try again!")

