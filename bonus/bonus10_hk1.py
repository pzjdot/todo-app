import random

from bonus10_function import parse

user_input = input("Enter lower bound and upper bound")
parsed = parse(user_input)
random_num = random.randint(parsed["lower_bound"], parsed["upper_bound"])
print(random_num)