"""
1. 提示用户输入新成员。

2. 将该成员添加到 members.txt 文件中现有成员的末尾。例如，这里的用户输入了成员 Solomon Right。
"""

import os

# 提示用户输入新成员
user_prompt = input("Enter new member: ")

# 构建基本目录
base_path = '/Users/pzj/PycharmProjects/pythonProject1/'
subfiles_path = os.path.join(base_path, 'mega/file/subfiles')

# 文件完整路径
full_path = os.path.join(subfiles_path, 'members.txt')
# 用with语句 写入文件
with open(full_path, 'a') as file:
    file.writelines(user_prompt + "\n")


with open(full_path, 'r') as file:
    user_list = file.readlines()

for item in user_list:
    print(item)

