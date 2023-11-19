# 检验密码是否为强弱密码
password = input("Enter your password")
result = {}

# 检验密码长度
if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False


# 检验密码中是否有数字
digital = False
for i in password:
    if i.isdigit():
        digital = True

result["digital"] = digital

# 检验密码中是否有大写
upper = False
for i in password:
    if i.isupper():
        upper = True
result["upper"] = upper

print(result)
# 检验长度 数字 大写 是否都符合
if all(result.values()):
    print("strong password")
else:
    print("weak password")



