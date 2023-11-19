string = 'skdaskerkjsalkj'
# 创建空字典
letter_count = {}

for letter in string:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

print(letter_count)

try:
    width = float(input("Enter rectangle width: "))
    length = float(input("Enter rectangle length: "))

    if width == length:
        exit("That looks like a square")

    area = width * length
    print(area)
except ValueError:
    print("Please enter a number")


waiting_list = ["john", "marry"]
name = input("Enter name: ")
try:

    number = waiting_list.index(name)

    print(f"{name}'s turn is {number}")
except ValueError:
    print("The name you entered is not in the list")

