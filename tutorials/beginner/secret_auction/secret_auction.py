from secret_auction_logo import logo

print(logo)
people_dict = {}
continue_bid = True

while continue_bid:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    people_dict[name] = bid
    response = input("Do you want to add another person? Yes or No").lower()

    highest_bid = 0

    if response == 'no':
        continue_bid = False
        for key, value in people_dict.items():
            if value > highest_bid:
                highest_bid = value

        print(f"{key} won the bid with {highest_bid}")
