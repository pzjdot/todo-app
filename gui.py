import time
import functions
import PySimpleGUI as sg


def add_todo(todo):
    todos.append(todo + "\n")
    functions.write_todos(todos)


def remove_to_todos(index):
    del todos[index]
    functions.write_todos(todos)


def update_to_todos():
    window["todo_list"].update(values=todos)
    window["todo"].update(value="")


def edit_to_todo(todo, index):
    todos[index] = todo + "\n"
    functions.write_todos(todos)


def select_todo(todo):
    window["todo"].update(value=todo)


todos = functions.get_todos()
sg.theme("LightBlue2")

layout = [
    [sg.Text("", key="clock")],
    [sg.Text("My To-Do App", font=("PingFang SC", 20))],
    [sg.InputText(tooltip="Enter To-Do", size=42, key="todo"), sg.Button(key="add", image_source="add.png",
                                                                         mouseover_colors="LightBlue2")],
    [sg.Listbox(values=functions.get_todos(), key="todo_list", size=(45, 10), enable_events=True,
                font=("PingFang SC", 16))],

    [sg.Button("edit", key="edit"), sg.Button(key="complete", image_source="complete.png",
                                              mouseover_colors="LightBlue2"), sg.Button("exit", key="exit")]
]


window = sg.Window("My To-Do App", layout=layout, font=("PingFang SC", 16))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    if event == sg.WIN_CLOSED:
        break

    if event == "add":
        add_todo(values["todo"])
        update_to_todos()

    elif event == "edit":
        if values["todo_list"]:
            edit_to_todo(values["todo"], todos.index(values["todo_list"][0]))
            update_to_todos()
        else:
            sg.popup("Please select an item first", font=("PingFang SC", 15), text_color="Yellow")

    elif event == "complete":
        if values["todo_list"]:
            remove_to_todos(todos.index(values["todo_list"][0]))
            update_to_todos()
        else:
            sg.popup("Please select an item first", font=("PingFang SC", 15), text_color="Yellow")

    elif event == "todo_list":
        select_todo(values["todo_list"][0])

    elif event == "exit":
        break

window.close()

