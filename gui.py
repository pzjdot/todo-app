import os.path

import PySimpleGUI as sg
import functions
import time
import os
sg.theme("DarkTeal2")
todos = functions.get_todos()

if not os.path.exists("todos.txt"):
    pass

layout = [
    [sg.Text("", key="clock")],
    [sg.Text("My To-Do App")],
    [sg.InputText(tooltip="Enter todo", key="todo", size=42), sg.Button(size=2, image_source="add.png",
                                                                        mouseover_colors="LightBlue2",
                                                                        tooltip="add todo", key="add")],

    [sg.Listbox(values=functions .get_todos(), key="todos",
                enable_events=True, size=(45, 10))],
    [sg.Button("edit"), sg.Button(size=2, image_source="complete.png", mouseover_colors="LightBlue2",
                                  tooltip="complete todo", key="complete"),
     sg.Text(key="Error", size=28), sg.Button("exit")]

]

window = sg.Window("My To-Do App", layout=layout, font=("Helvetica", 15))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "add":
            new_todos = (
                     values["todo"] + "\n")
            todos.append(new_todos)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
            window["Error"].update(value="")

        case "edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]

                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("please select an item first", title="Error",
                         font=("Helvetica", 15), text_color="Yellow")

        case "complete":
            try:
                todo_to_edit = values["todos"][0]
                todos.remove(todo_to_edit)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("please select an item first", title="Error",
                         font=("Helvetica", 15), text_color="Yellow")

        case "todos":
            window["todo"].update(value=values['todos'][0])

        case "exit":
            break

        case sg.WIN_CLOSED:
            break

window.close()
