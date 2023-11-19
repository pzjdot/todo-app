import PySimpleGUI as sg

# 自定义布局
layout = [
    [sg.Text("Select to files to compress"), sg.Input(), sg.FilesBrowse("choose")],
    [sg.Text("Select to destination folder"), sg.Input(), sg.FolderBrowse("choose")],
    [sg.Button("compress")]
]

window = sg.Window("Zip", layout=layout)
window.read()
window.close()