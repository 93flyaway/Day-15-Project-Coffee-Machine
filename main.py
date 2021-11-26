from menu import MENU, resources


COIN_VALUE = {
        "quarters": 0.25,
        "dimes": 0.1,
        "nickels": 0.05,
        "pennies": 0.01,
}


# TODO: 3. Print report.
# a. When the user enters “report” to the prompt,
# a report should be generated that shows the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5


def print_report(balance):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${balance}")


# TODO: 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.
def is_enough_resources(drink):
    """prints 'Sorry there is not enough {ingredient.}' when lacking ingredients. Returns True if enough resources
    and False if there aren't enough resources."""
    ingredients = MENU[drink]["ingredients"]
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def sum_coins(current_coins):
    """returns total value of a dictionary of coin values"""
    coin_sum = 0

    for coin in current_coins:
        coin_sum += current_coins[coin] * COIN_VALUE[coin]
    return coin_sum


def deduct_resources(drink):
    ingredients = MENU[drink]["ingredients"]
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]


# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.


def coffee_machine():
    is_power_on = True
    money = 0

    while is_power_on:
        user_drink = input(" What would you like? (espresso/latte/cappuccino): ").lower()
# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    # a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
    # the machine. Your code should end execution when this happens.
        if user_drink == 'off':
            return
        elif user_drink == "report":
            print_report(money)
        else:
            if is_enough_resources(user_drink):
                print("Please insert coins.")
                user_quarters = int(input("how many quarters?: "))
                user_dimes = int(input("how many dimes?: "))
                user_nickels = int(input("how many nickels?: "))
                user_pennies = int(input("how many pennies?: "))
                user_coins = {
                    "quarters": user_quarters,
                    "dimes": user_dimes,
                    "nickels": user_nickels,
                    "pennies": user_pennies,
                }
                user_money = sum_coins(user_coins)
                drink_cost = MENU[user_drink]["cost"]

                if user_money < drink_cost:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    money += drink_cost
                    if user_money > drink_cost:
                        change = user_money - drink_cost
                        formatted_change = "{:.2f}".format(change)
                        print(f"Here is ${formatted_change} in change.")
                    deduct_resources(user_drink)
                    print(f"Here is your {user_drink}. Enjoy!")


coffee_machine()


# TODO: 5. Process coins.
# a. If there are sufficient resources to make the drink selected,
# then the program should prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52


# TODO: 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program should say
# “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit
# and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.


# TODO: 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink.
