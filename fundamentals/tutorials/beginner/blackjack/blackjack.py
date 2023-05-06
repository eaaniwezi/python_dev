import random
import os
from blackjack_logo import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def play_game():
    user_card = []
    computer_card = []
    is_game_over = False


    def calculate_score(card_list):
        if sum(card_list) == 21 and len(card_list) == 2:
            return 0
        if 11 in card_list and sum(card_list) > 21:
            card_list.remove(11)
            card_list.append(1)
        return sum(card_list)


    for x in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())


    def compare(user_score, computer_score):

        if user_score == computer_score:
            return ("draw")
        elif computer_score == 0:
            return("You loss")
        elif user_score == 0:
            return("You win")
        elif user_score > 21:
            return("You loss")
        elif computer_score > 21:
            return("You win")
        else:
            highest = max(user_score, computer_score)
            if highest == computer_score:
                return("You loss")
            else:
                return("You win")


    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f" Your cards: {user_card}, current score: {user_score}")
        print(f"  Computer's first card: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            another_card = input(
                "Type 'y' to get another card, type 'n' to pass: ").lower()
            if another_card == 'y':
                user_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f" Your final hand: {user_card}, final score: {user_score}")
    print(
        f" Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Yes or No").lower() == "yes":
    os.system('cls||clear')
    print(logo)
    play_game()


