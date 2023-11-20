import PySimpleGUI as sg
import functions

layout = [
    [sg.Text("My To-Do App")],
    [sg.InputText(tooltip="Enter todo", key="todo"), sg.Button("add")]
]

window = sg.Window("My To-Do App", layout=layout, font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "add":
            todos = functions.get_todos()
            new_todos = values["todo"] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()