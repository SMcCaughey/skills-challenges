from lib.todo import Todo, TodoList

def test_add_todo_to_list():
    todo_list = TodoList()
    todo = Todo("Buy milk")
    todo_list.add(todo)
    assert todo in todo_list.todo

def test_incomplete_returns_only_incomplete_todos():
    todo_list = TodoList()
    todo1 = Todo("Task 1")
    todo2 = Todo("Task 2")
    todo2.mark_complete()
    todo_list.add(todo1)
    todo_list.add(todo2)
    assert todo_list.incomplete() == [todo1]

def test_complete_returns_only_complete_todos():
    todo_list = TodoList()
    todo1 = Todo("Task 1")
    todo2 = Todo("Task 2")
    todo2.mark_complete()
    todo_list.add(todo1)
    todo_list.add(todo2)
    assert todo_list.complete() == [todo2]

def test_give_up_marks_all_todos_complete():
    todo_list = TodoList()
    todo1 = Todo("Task 1")
    todo2 = Todo("Task 2")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.give_up()
    assert todo1.complete is True
    assert todo2.complete is True