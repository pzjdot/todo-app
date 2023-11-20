import os


# 构建到子目录的基础路径
base_path = '/Users/pzj/PycharmProjects/pythonProject1'
subfiles_path = os.path.join(base_path, 'mega/file/subfiles')

contents = ["pzj like fy", "fy like pzj", "fy and pzj forever"]
filenames = ["doc.txt", "report.txt", "presentation.txt"]

# 为每个文件构建完整路径并写入内容
for content, filename in zip(contents, filenames):
    full_path = os.path.join(subfiles_path, filename)

    with open(full_path, 'w') as files:
        files.write(content + "\n")

