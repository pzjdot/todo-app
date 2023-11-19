import random


def random_num(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)

        if num1 > num2:
            num1, num2 = num2, num1

        return random.randint(num1, num2)
    except ValueError:
        return "Please enter valid numbers"


number1 = input("Enter first number")
number2 = input("Enter second number")
random_number = random_num(number1, number2)
print(random_number)

