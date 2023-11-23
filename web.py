import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state.new_todo
    if new_todo:
        todos.append(new_todo + "\n")
        functions.write_todos(todos)

    st.session_state.new_todo = ""


def main():
    st.title("To-Do APP")
    st.subheader("This app is to increase your productivity")

    global todos
    todos = functions.get_todos()
    is_changed, process_todo = process_todos(todos)

    if is_changed:
        functions.write_todos(process_todo)
        st.experimental_rerun()

    st.text_input(label="", placeholder="add new add...", on_change=add_todo, key="new_todo")


def process_todos(process_todo):
    todos_changed = False
    marked_for_deletion = [index for index, todo in enumerate(process_todo) if st.checkbox(todo, key=index)]
    if marked_for_deletion:
        process_todo = [todo for index, todo in enumerate(process_todo) if index not in marked_for_deletion]
        todos_changed = True
    return todos_changed, process_todo


if __name__ == '__main__':
    main()