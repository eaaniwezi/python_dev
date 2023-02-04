
import os
import random
from higher_lower_logo import logo, vs
from higher_lower_game_data import data

score = 0
game_over = False
 
def intro():
    print(logo)
    first_question = random.choice(data)
    second_question = random.choice(data)
    print(f"Compare A: {first_question['name']}, a/an {first_question['description']}, from {first_question['country']} score {first_question['follower_count']}")
    print(vs)
    print(f"Against B: {second_question['name']}, a/an {second_question['description']}, from {second_question['country']} score {second_question['follower_count']}")
    
    return [first_question, second_question]



def compare():
    questions = intro()
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    first_question = questions[0]
    second_question = questions[1]
    most_popular = max(first_question['follower_count'], second_question['follower_count'])
    # print(f"\n\nthe most {questions}")
    if answer == 'A' and most_popular == first_question['follower_count']:
        global score
        score += 1
        os.system('cls||clear')
        print(f"You are right! Current score: {score}")
    elif answer == 'B' and most_popular == second_question['follower_count']:
        # global score
        score += 1
        os.system('cls||clear')
        print(f"You are right! Current score:: {score}")
    else:
        global game_over
        game_over = True
        score = 0
        os.system('cls||clear')
        print(f"\nYou are wrong! You chose {answer}")
    

while not game_over:
    compare()