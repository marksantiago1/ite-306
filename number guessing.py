import random

secret_number = random.randint(1,10) 

attempts = 0

print("Welcome to the Guessing Game Number")

while True:
    user = int(input("Guess the Number (Between 1 to 10): "))
    attempts +-1 
    if user < secret_number:
        print("The number you have guess is low.")
    elif user < secret_number:
        print("The number you have guess is high ")
    else:
        print("Congratulations your guess is correct!")