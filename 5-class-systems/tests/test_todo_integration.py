from lib.todo import Todo, TodoList

def test_add_and_retrieve_todos_integration():
    todo_list = TodoList()
    todo1 = Todo("Walk the dog")
    todo2 = Todo("Read a book")
    todo_list.add(todo1)
    todo_list.add(todo2)
    assert todo_list.incomplete() == [todo1, todo2]
    assert todo_list.complete() == []

def test_mark_todo_complete_and_check_lists():
    todo_list = TodoList()
    todo1 = Todo("Do laundry")
    todo2 = Todo("Call mom")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo1.mark_complete()
    assert todo_list.incomplete() == [todo2]
    assert todo_list.complete() == [todo1]

def test_give_up_marks_all_complete_integration():
    todo_list = TodoList()
    todo1 = Todo("Task A")
    todo2 = Todo("Task B")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.give_up()
    assert todo_list.incomplete() == []
    assert todo_list.complete() == [todo1, todo2]