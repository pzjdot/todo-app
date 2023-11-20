# from functions import get_todos, write_todos
import functions

while True:
    user_action = input("type add, show, edit, complete or exit: ")
    # remove leading and trailing to ensure user input does not contain spaces
    user_action = user_action.strip()

    if user_action.startswith("add"):
        """
        todo = input("Enter a todo: ") + "\n"
        with open('todos.txt', 'a') as file:
            file.writelines(todo)
        """

        todo = user_action[4:]

        todos = functions.get_todos()  # invoke the function to read a file

        # continue appending new code items to the list after adding the existing to-do items
        todos.append(todo + "\n")

        functions.write_todos(todos_list=todos)

    elif user_action.startswith("show"):
        # invoke the function to read a file
        todos = functions.get_todos()

        """
        list comprehension to remove empty line characters
        new_content = [item.strip("\n") for item in content]
        """

        # Iterate the list returned by file reading function
        for index, item in enumerate(todos):
        
            row = f"{index + 1}.{item.strip("\n")}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            index = number - 1

            todos = functions.get_todos()  # invoke the function to read a file

            # modify the value at the corresponding index in the file
            new_todo = input("Enter new todo.txt: ")
            todos[index] = new_todo + "\n"

            functions.write_todos(todos_list=todos)

        except ValueError:
            print("Invalid edit command format. Please use: edit <number>")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()  # invoke the function to read a file

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos_list=todos)

            message = f"todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue
        except ValueError:
            print("Invalid edit command format. Please use: complete <number>")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("command is not valid")


