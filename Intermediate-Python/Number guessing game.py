import random

secret_number = random.randint(1, 10)

guess = int(input('Guess a number between 1-10: '))

#Check if correct 
if guess == secret_number:
    print(f'Correct! the number was: {secret_number}')
else:
    print(f'Wrong! the correct number was: {secret_number}')
