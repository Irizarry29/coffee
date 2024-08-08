# Recipe for each beverage.

coffee_menu = {
    "cappuccino": 3.00,
    "espresso": 1.50,
    "latte": 2.50,
}

coffee_recipes = {
    "cappuccino": {
        "water": 250,
        "coffee": 24,
        "milk": 100,
        # "cost": 3.00,
    },
    "espresso": {
        "water": 50,
        "coffee": 18,
        # "cost": 1.50,
    },
    "latte": {
        "water": 200,
        "coffee": 24,
        "milk": 150,
        # "cost": 2.50,
    },
}


def get_coffee_choice():
    global coffee_menu
    print("=====================================================")
    print("Menu:")
    for (coffee, price) in coffee_menu.items():
        print(f"{coffee}, ${price:.2f}")
    customer_choice = input(f"What would you like to drink? \n")
    return customer_choice.lower()


def dispense_coffee():
    print("Dispensing coffee.")


def generate_report(available_resources):
    """Displays remaining ingredients and what the profit is."""

    print(f"water: {available_resources['water']}{'ml'}")
    print(f"milk: {available_resources['milk']}{'ml'}")
    print(f"coffee: {available_resources['coffee']}{'g'}")


def get_recipe(coffee):
    ingredients = []
    espresso_recipe = {
        "water": 50,
        "coffee": 18,
        # "cost": 1.50,
    }
    latte_recipe = {
        "water": 200,
        "coffee": 24,
        "milk": 150,
        # "cost": 2.50,
    }
    cappuccino_recipe = {
        "water": 250,
        "coffee": 24,
        "milk": 100,
        # "cost": 3.00,
    }
    if coffee == "espresso":
        ingredients = espresso_recipe
    elif coffee == "latte":
        ingredients = latte_recipe
    elif coffee == "cappuccino":
        ingredients = cappuccino_recipe
    return ingredients


def calc_missing_ingredients(needs, on_hand):
    missing = []
    return missing


def get_money():
    coins = {
        "quarter": 0.25,
        "dime": 0.10,
        "nickel": 0.05,
        "penny": 0.01,
    }
    print("Please insert Coins.")
    number_of_quarters = int(input("How many quarters?: "))
    number_of_dimes = int(input("How many dimes?: "))
    number_of_nickels = int(input("How many nickels?: "))
    number_of_pennies = int(input("How many pennies?: "))
    money_received = (number_of_quarters * 0.25
                      + number_of_dimes * 0.10
                      + number_of_nickels * 0.05
                      + number_of_pennies * 0.01)
    money_received = round(money_received, 2)
    print(f"You inserted ${money_received:.2f}.")
    return money_received


def get_price(coffee):
    global coffee_menu
    price = coffee_menu[coffee]
    return price


def reduce_inventory(inventory, ingredients):
    new_inventory = inventory
    return new_inventory


def handle_payment(price):
    """Get coins and give change. Returns true if sufficent funds"""
     # 5. Process coins
    print(f"please insert ${price:.2f}")
    money = get_money()
    # 6. Check transaction successful
    if money < price:
        print("Insufficient funds")
        print(f"Here is your money back ${money:.2f}")
        return False
    if money > price:
        change = round(money - price, 2)
        print(f"Here is your change ${change:.2f}") 
        return True
    if money == price:
        return True


def main():
    inventory = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    while True:
        # 1.Get customer choice
        customer_choice = get_coffee_choice()
        # 2. Turns off machine
        if customer_choice == "off":
            break
        # 3. Prints report
        if customer_choice == "report":
            generate_report(inventory)
        if customer_choice not in coffee_recipes:
            print("Sir this is starbucks. Please order some coffee.")
            continue
        # 4. Check ingredients
        ingredients_for_customer_drink = get_recipe(customer_choice)
        print("The ingredients are:", ingredients_for_customer_drink)
        needed_ingredients = calc_missing_ingredients(
            ingredients_for_customer_drink, inventory)
        if len(needed_ingredients) > 0:
            print(needed_ingredients)
            break
        sufficient_funds = handle_payment(get_price(customer_choice))
        # 7. Make the Coffee, reduce ingredients
        if sufficient_funds == True:
            inventory = reduce_inventory(inventory, ingredients_for_customer_drink)
            dispense_coffee()
        


if __name__ == "__main__":
    main()

# TODO: report should show current money earned
# TODO: Inventory should be reduced when coffee is made
# TODO: Fix Caps on Menu