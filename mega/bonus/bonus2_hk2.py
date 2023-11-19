"""
1. 提示用户输入新成员。

2. 将该成员添加到 members.txt 文件中现有成员的末尾。例如，这里的用户输入了成员 Solomon Right。
"""


# 提示用户输入新成员
user_prompt = input("Enter new user: ")

with open('../file/subfiles/members.txt', 'r') as file1:
    user_list = file1.readlines()

user_list.append(user_prompt + "\n")


with open('../file/subfiles/members.txt', 'w') as file2:
    file2.writelines(user_list)

for item in user_list:
    print(item)