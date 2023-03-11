# from coffee_machine_data import MENU, resources

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


balance = 0


def insert_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def check_resources(order_ingredents):
    for item in order_ingredents:
        if order_ingredents[item] > resources[item]:
            print(f"Sorry there is no enough {item}")
            return False
    return True


def is_transaction_successful(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global balance
        balance += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


check_available_resources = True


def process_order():
    order = input("What would you like? (espresso/latte/cappuccino):\nType 'report' to see available resources: ")

    if order == 'off':
        check_available_resources = False
    elif order == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${balance}")
    else:
        drink = MENU[order]
        if check_resources(drink['ingredients']):
            payment = insert_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(order, drink['ingredients'])
        print(drink)


process_order()
