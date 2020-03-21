import math

print(
    "Would you like to add,subtract,divide and multiple numbers "
    "or would you like to find the area, radius and circumference of a circle?")
print("------------------")
print("""Enter:
1: to add,subtract,divide or multiple numbers
2: to calcualte a circle""")
print("-------------------")
decide = input("please enter 1 or 2")


def add(ask):
    add = 0
    for j in range(ask):
        number = int(input("Number: "))
        add = add + number
    return add


def subtract(ask):
    count = 0
    for j in range(ask):
        count += 1
        number = int(input("Number:"))
        if count == 1:
            add = number
        else:
            add = add - number
    return add


def mull(ask):
    add = 1
    for j in range(ask):
        number = int(input("Number: "))
        add = add * number
    return add


def div(ask):
    add = 1
    count = 0
    for j in range(ask):
        count += 1
        number = int(input("Number: "))
        if count == 1:
            add = number
        else:
            add = add / number
    return add


def calculator():
    while True:
        op = input("How would you like to calculate")
        if op == "+":
            print(add(ask))
            break
        elif op == "-":
            print(subtract(ask))
            break
        elif op == "*":
            print(mull(ask))
            break
        elif op == "/":
            print(div(ask))
            break
        else:
            print("Invalid operator, please enter the correct operator")


def circle():
    print(
        "In order to calculate the area of a circle, the circumference, radius or the diameter of the circle is needed.")
    print("""Enter: 
  1: for circumference
  2: for radius
  3: for diameter""")
    info = int(input("Please enter which information you have"))
    while True:
        if info == 1:
            circumference = float(input("Please enter the circumference of the circle"))
            area = circumference ** 2 / (4 * math.pi)
            return area
        elif info == 2:
            radius = float(input("Please enter the radius of the circle"))
            area = math.pi * (radius ** 2)
            return area
        elif info == 3:
            diameter = float(input("Please enter the diameter of the circle"))
            area = (math.pi * (diameter ** 2)) / 4
        else:
            print("please enter 1, 2, or 3")

        return area


if decide == "1":
    while True:
        try:
            ask = int(input("How many numbers would you like to calculate"))
        except ValueError:
            print("Please enter a number")
        else:
            print(calculator())
            break
elif decide == "2":
    print("The area of the circle is " + str(circle()))
else:
    print("please enter 1 or 2")
