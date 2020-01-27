class CoffeeMachine:
    def __init__(self, coffee, milk, water, money, cups):
        self.coffee = coffee  # 120
        self.water = water  # 1200
        self.cups = cups  # 9
        self.milk = milk  # 540
        self.money = money  # 550


coffee = CoffeeMachine(120, 540, 1200, 550, 9)


def current_supply():
    global coffee
    print()
    print("The coffee machine has: ")
    print(coffee.water, "of water")
    print(coffee.milk, "of milk")
    print(coffee.coffee, "of coffee beans")
    print(coffee.cups, "of disposable cups")
    print(coffee.money, "of money\n")


def buy():
    global coffee
    coffee_type = ["espresso", "latte", "cappuccino"]
    case = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
    if coffee.coffee >= 0 and coffee.water >= 0 and coffee.water >= 0 and coffee.milk >= 0:
        if case == 1:
            coffee.coffee -= 16
            coffee.water -= 250
            coffee.money += 4
        elif case == 2:
            coffee.coffee -= 20
            coffee.water -= 350
            coffee.milk -= 75
            coffee.money += 7
        elif case == 3:
            coffee.coffee -= 12
            coffee.water -= 200
            coffee.milk -= 100
            coffee.money += 6
        coffee.cups -= 1
    else:
        print("There is no need supply")
    current_supply()


def fill():
    global coffee
    try:
        coffee.water += int(input("Write how many ml of water do you want to add: "))
        coffee.milk += int(input("Write how many ml of milk do you want to add: "))
        coffee.coffee += int(input("Write how many grams of coffee beans do you want to add: "))
        coffee.cups += int(input("Write how many disposable cups of coffee do you want to add: "))
    except ValueError:
        print("Sorry, there is exception. Incorrect input.")
    current_supply()


def take():
    global coffee
    print("I gave you $", coffee.money, sep="")
    coffee.money = 0
    current_supply()


def main():
    current_supply()
    choice = input("Write action (buy, fill, take): ")
    if choice == "buy":
        buy()
    elif choice == "fill":
        fill()
    elif choice == "take":
        take()


main()
