class CoffeeMachine:
    """Basic class that represent functionality of coffee machine"""
    number_machine = 0

    def __init__(self, coffee_beans, milk, water, money, cups):
        self.coffee_beans = coffee_beans
        self.water = water
        self.cups = cups
        self.milk = milk
        self.money = money

    def __str__(self):
        """Basic output of information."""
        print("Coffee machine work correct. Current supply: water - {}, milk - {}, coffee beans - {}, cups - {}".format(self.water, self.milk, self.coffee_beans, self.cups))

    def current_supply(self):
        global coffee
        print()
        print("The coffee machine has: ")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.coffee_beans, "of coffee beans")
        print(self.cups, "of disposable cups")
        print("$", self.money, " of money", sep="")


def enough_supply(coffee_beans, water, milk, cups, money):
    global coffee
    if coffee.coffee_beans - coffee_beans < 0 or coffee.water - water < 0 or coffee.milk - milk < 0 or coffee.cups - cups < 0:
        print("Sorry, not enough water!")
    else:
        coffee.coffee_beans -= coffee_beans
        coffee.water -= water
        coffee.milk -= milk
        coffee.cups -= cups
        coffee.money += money
        print("I have enough resources, making you a coffee.")


def buy():
    global coffee
    coffee_type = ["espresso", "latte", "cappuccino"]
    case = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
    if case == "1":
        enough_supply(16, 250, 0, 1, 4)
    elif case == "2":
        enough_supply(20, 350, 75, 1, 7)
    elif case == "3":
        enough_supply(12, 200, 100, 1, 6)
    elif case == "back":
        return "back"


def fill():
    global coffee
    try:
        coffee.water += int(input("\nWrite how many ml of water do you want to add: "))
        coffee.milk += int(input("Write how many ml of milk do you want to add: "))
        coffee.coffee_beans += int(input("Write how many grams of coffee beans do you want to add: "))
        coffee.cups += int(input("Write how many disposable cups of coffee do you want to add: "))
    except ValueError:
        print("Sorry, there is exception. Incorrect input.")


def take():
    global coffee
    print("\nI gave you $", coffee.money, sep="")
    coffee.money = 0


def main():
    global coffee
    actions = ["buy", "fill", "take", "remaining", "exit"]
    while True:
        choice = input("\nWrite action (buy, fill, take, remaining, exit): ")
        if choice in actions:
            if choice == "buy":
                if buy() == "back":
                    continue
            elif choice == "fill":
                fill()
            elif choice == "take":
                take()
            elif choice == "remaining":
                coffee.current_supply()
            elif choice == "exit":
                break


coffee = CoffeeMachine(120, 540, 400, 550, 9)
main()
