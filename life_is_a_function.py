def circle_area(radius):
    pi = 3.14159
    area = pi * radius ** 2
    return area


def calculate_taxes(money, tax):
    total_due = money + (money * tax)
    return total_due


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius


radius = float(input("Enter the radius: "))
area = circle_area(radius)
print(f"{area:.2f}")

money = float(input("Enter the amount of money: "))
tax = float(input("Enter the tax rate: "))
total = calculate_taxes(money, tax / 100)
print(f"{total:.2f}")

fahrenheit = float(input("Enter the Fahrenheit temperature: "))
temperature = fahrenheit_to_celsius(fahrenheit)
print(f"{temperature:.4f}")