MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 250,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 150,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 200,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

def is_reource_sufficient(order_ingr):
    is_enough = True
    for item in order_ingr:
        if order_ingr[item] >= resources[item]:
            print(f'Sorry there is not enough {item}.')
            is_enough = False
            
    return is_enough

def process_coins():
    print("Please Insert Coins")
    total = int(input("How many Php 10?: ")) * 10
    total += int(input("How many Php 50?: ")) * 50 
    total += int(input("How many Php 100?: ")) * 100
    return total

def is_transaction_successful(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        global profit
        profit = profit + money_recieved
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is Php {change} in change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

def make_coffe(drink_name, order_ingr):
    for item in order_ingr:
        resources[item] -= order_ingr[item]
    print(f'Here is your {drink_name}')


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'off':
        is_on = False
    
    elif choice == "report":
        print(f'Water: {resources["water"]}')
        print(f'Milk: {resources["milk"]}')
        print(f'Coffee: {resources["coffee"]}')
        print(f'Money: Php{profit}')
    
    else:
        drink = MENU[choice]
        if is_reource_sufficient(drink["ingredients"]):
            payment = process_coins()
            print(f"Payment: Php {payment}")
            if is_transaction_successful(payment, drink["cost"]):
                make_coffe(choice, drink["ingredients"])
        
