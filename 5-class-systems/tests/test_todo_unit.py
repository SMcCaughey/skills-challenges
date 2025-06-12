from lib.todo import Todo

def test_todo_initial_state_is_incomplete():
    todo = Todo("Write tests")
    assert todo.task == "Write tests"
    assert todo.complete is False

def test_mark_complete_sets_complete_true():
    todo = Todo("Finish project")
    todo.mark_complete()
    assert todo.complete is True

def test_mark_complete_idempotent():
    todo = Todo("Refactor code")
    todo.mark_complete()
    todo.mark_complete()
    assert todo.complete is True
