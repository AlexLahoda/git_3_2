import math


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Немає такої операції."
    return x / y


def exponentiation(x, y):
    return x ** y


def square_root(x):
    return math.sqrt(x)


def cube_root(x):
    return x ** (1/3)


print("Виберіть опцію:")

while True:
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    print("5. Зведення в ступінь")
    print("6. Квадратний корінь")
    print("7. Кубічний корінь")
    print("8. Вихід")
    op = int(input("Ваш вибір (1-8):"))

    if op == 1:
        num1 = float(input("Введіть число: "))
        num2 = float(input("Введіть друге число: "))
        print(add(num1, num2))
        print("\n")

    elif op == 2:
        num1 = float(input("Введіть число: "))
        num2 = float(input("Введіть друге число: "))
        print(subtract(num1, num2))
        print("\n")

    elif op == 3:
        num1 = float(input("Введіть число: "))
        num2 = float(input("Введіть друге число: "))
        print(multiply(num1, num2))
        print("\n")

    elif op == 4:
        num1 = float(input("Введіть число: "))
        num2 = float(input("Введіть друге число: "))
        print(divide(num1, num2))
        print("\n")

    elif op == 5:
        num1 = float(input("Введіть число: "))
        num2 = float(input("Введіть друге число: "))
        print(exponentiation(num1, num2))
        print("\n")

    elif op == 6:
        num1 = float(input("Введіть число: "))
        print(square_root(num1))
        print("\n")

    elif op == 7:
        num1 = float(input("Введіть число: "))
        print(cube_root(num1))
        print("\n")

    elif op == 8:
        break

    else:
        print("Немає такої опції.")
        print("\n")
