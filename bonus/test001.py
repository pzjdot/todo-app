user_prompt = "Enter a todo.txt"

todos = []

while True:
    todo = input(user_prompt)

    # capitalize  会让单词首字母大写， 我输入 clean，会返回Clean
    new_todo = todo.capitalize()

    # title 它会找到字符串中所有的单词并且将每个单词的开头变成大写，我输入 fy i like you，会返回 Fy I Like You
    new_todo2 = todo.title()

    todos.append(new_todo2)
    print(todos)
