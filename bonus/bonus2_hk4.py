"""然后，创建一个程序：

1.读取每个文本文件并

2.在命令行中打印出每个文件的内容。"""
import os.path

import os.path

base_path = "/Users/pzj/PycharmProjects/pythonProject1"
subfiles_path = os.path.join(base_path, 'mega/file/subfiles')

files = ["a.txt", "b.txt", "c.txt"]

for item in files:
    full_path = os.path.join(subfiles_path, item)
    with open(full_path, 'r') as file:
        my_list = file.readlines()
        print(my_list)
