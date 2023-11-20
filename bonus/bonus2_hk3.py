"""

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

然后，创建一个程序：

1.通过迭代列表生成多个文本文件filenames，

2. 并将文本Hello  写入每个生成的文本文件中。

"""
import os.path

# 构建基础目录
base_path = '/Users/pzj/PycharmProjects/pythonProject1'
subfiles_path = os.path.join(base_path, 'mega/file/subfiles')

filenames = ['doc.txt', 'report.txt', 'presentation.txt']


for filename in filenames:
    full_path = os.path.join(subfiles_path, filename)
    with open(full_path, 'w') as file:
        file.write("Hello")
