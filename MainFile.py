def current_supply():
    global coffee, water, money, milk, cups
    print()
    print("The coffee machine has: ")
    print(water, "of water")
    print(milk, "of milk")
    print(coffee, "of coffee beans")
    print(cups, "of disposable cups")
    print(money, "of money\n")


def buy():
    global coffee, water, money, milk, cups
    case = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappucino: "))
    if case == 1:
        coffee -= 16
        water -= 250
        money += 4
    elif case == 2:
        coffee -= 20
        water -= 350
        milk -= 75
        money += 7
    elif case == 3:
        coffee -= 12
        water -= 200
        milk -= 100
        money += 6
    cups -= 1
    current_supply()


def fill():
    global coffee, water, money, milk, cups
    water += int(input("Write how many ml of water do you want to add: "))
    milk += int(input("Write how many ml of milk do you want to add: "))
    coffee += int(input("Write how many grams of coffee beans do you want to add: "))
    cups += int(input("Write how many disposable cups of coffee do you want to add: "))
    current_supply()


def take():
    global money
    print("I gave you $", money, sep="")
    money = 0
    current_supply()


coffee = 120
water = 1200
cups = 9
milk = 540
money = 550


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