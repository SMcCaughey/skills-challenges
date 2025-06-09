class Tracker():

    def __init__(self):
        self._tasks = []
        
    def add_task(self, task):
        if task == "":
            raise Exception("Don't be lazy!")
        self._tasks.append(task)
    
    def complete_task(self, task):
        if task not in self._tasks:
            raise Exception("Not on list.")
        self._tasks.remove(task)
    
    def todo(self):
        return self._tasks