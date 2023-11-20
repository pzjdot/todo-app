# 输入inch feet 转换成 meter
from bonus.convert8 import convert
from bonus.parse8 import parse

feet_inches = input("Enter feet and inch: ")

parsed = parse(feet_inches)

result = convert(parsed["feet"], parsed["inch"])

print(f"{parsed["feet"]} feet and {parsed["inch"]} is equals to {result}")

if result < 1:
    print("kid is too small")
else:
    print("kid can use the slide")
