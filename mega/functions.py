import os.path
# 基本路径
base_path = '/Users/pzj/PycharmProjects/todo_app'
subfiles_path = os.path.join(base_path, "mega")
full_path = os.path.join(subfiles_path, 'todos.txt')


def get_todos(path=full_path):
    """ Read a text file and return the list of
    to-do items
    """
    with open(path, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_list, path=full_path):
    """ Write the to-do items list in the text file"""
    with open(path, 'w') as file_local:
        todos_local = file_local.writelines(todos_list)
    return todos_local


if __name__ == "__main__":
    print("hello")
