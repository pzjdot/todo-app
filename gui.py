import PySimpleGUI as sg
import functions

todos = functions.get_todos()

layout = [
    [sg.Text("My To-Do App")],
    [sg.InputText(tooltip="Enter todo", key="todo"), sg.Button("add")],
    [sg.Listbox(values=functions.get_todos(), key="todos",
                enable_events=True, size=(45, 10))],
    [sg.Button("edit"), sg.Button("complete")]

]

window = sg.Window("My To-Do App", layout=layout, font=("Helvetica", 15))

while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "add":
            new_todos = values["todo"] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]

            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "complete":
            todo_to_edit = values["todos"][0]
            index = todos.index(todo_to_edit)
            todos.pop(index)
            window["todos"].update(values=todos)

        case "todos":
            window["todo"].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()
