# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        self.todo = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.todo.append(todo)

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        incomplete_tasks = []
        for todo in self.todo:
            if not todo.complete:
                incomplete_tasks.append(todo)
        return incomplete_tasks

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        complete_tasks = []
        for todo in self.todo:
            if todo.complete:
                complete_tasks.append(todo)
        return complete_tasks

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for todo in self.todo:
            todo.mark_complete()


# File: lib/todo.py
class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False
        self.task = task
        self.complete = False
        

    def mark_complete(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        self.complete = True
