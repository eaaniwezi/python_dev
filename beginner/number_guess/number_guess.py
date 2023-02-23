import random
from number_guess_logo import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and  100")


lives = 0
continue_game = True

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    lives = 10
    print(f"You have {lives} attempts remaining to guess the number")
else:
    lives = 5
    print(f"You have {lives} attempts remaining to guess the number")

raddom_guess = random.choice(range(1, 101))
print(f"The guess is: {raddom_guess}")

while continue_game:
    guess = int(input("Make a guess: "))

    if raddom_guess == guess:
        print("Correct")
        continue_game = False
    elif guess > raddom_guess and lives > 0:
        print('To high')
        lives -= 1
        print(f"You have {lives} attempts remaining to guess the number")
    elif guess < raddom_guess and lives > 0:
        lives -= 1
        print(f"You have {lives} attempts remaining to guess the number")
        print('To low')
    else:
        continue_game = False
        print(f"Game over!!! The number is {raddom_guess}")


