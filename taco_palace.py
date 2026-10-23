
def printMenu():
    print("\nWelcome to Taco Palace!")
    print("Please view the menu below and make a selection")
    print("\nTaco Palace Menu")
    print("1. Taco")
    print("2. Burrito")
    print("3. Nachos")
    print("4. Soft Drink")
    print("5. Quit")


def getPrice(choice):
    if choice == 1:
        return 3.50
    elif choice == 2:
        return 6.25
    elif choice == 3:
        return 5.00
    elif choice == 4:
        return 1.75


def getFood(choice):
    if choice == 1:
        return "Taco"
    elif choice == 2:
        return "Burrito"
    elif choice == 3:
        return "Nachos"
    elif choice == 4:
        return "Soft Drink"


orders = []
total = 0.0

while True:
    printMenu()

    try:
        choice = int(input("\nEnter your selection: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 5:
        break
    elif choice >= 1 and choice <= 4:
        food = getFood(choice)
        price = getPrice(choice)

        print("You selected a", food)

        orders.append(food)
        total = total + price
    else:
        print("Invalid selection. Please try again.")


print("\nYour order:")

if len(orders) == 0:
    print("You did not order anything.")
else:
    for food in orders:
        print("-", food)

print(f"Your total is ${total:.2f}")
