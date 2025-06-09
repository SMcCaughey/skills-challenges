# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

When Initialised, the class will have to store information for each object - notably a list of todo tasks, which can be altered by adding or removing certain entries, then printed/returned at any time.

"""
First, create the class Tracker, which we will then initialise with the list we want each tracker to have access to. The tasks property is set to private so that it can only be interacted with by the user through public methods.
"""

```python
class Tracker():

    def __init__(self):
        self._tasks = []

    def add_task(self, task):
        # Parameters 
            # task: (str) a sentence or phrase, may contain numbers or special characters.
        # Returns
            # Nothing
        # Side-Effects
            # Adds parameter to list in init
    
    def complete_task(self, task):
        # Parameters
            # task: (str) a sentence or phrase already in self._tasks, may contain numbers or special characters.
        # Returns
            # Nothing
        # Side-Effects
            # Removes parameter from list in init
    
    def todo(self):
        # Parameters
            # None
        # Returns
            # self._tasks (list) a list of tasks that have yet to be finished, manipulated by other methods.
        # Side Effects
            # None
```

_Make a list of examples of how the class will behave in different situations._

```python

"""
Given a task
# Adds task to list
"""
jobs = Tracker()
jobs.add_task("first")
jobs.todo() => ["first"]

"""
Given an empty input
# Raises Exception - "Don't be lazy!"
"""
jobs = Tracker()
jobs.add_task("") => "Don't be lazy!"

"""
Given a task on the list is completed
# Removes task from the list
"""
jobs = Tracker()
jobs.complete_task("first")
jobs.todo() => []

"""
Given a task that is not on the list is completed
# Raises exception "Not on list."
"""
jobs = Tracker()
jobs.complete_task("second") => "Not on list."

"""
Bring up the todo list
# Returns self.tasks
"""
jobs = Tracker()
jobs.todo() => []

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

```python

from lib.todo import *
import pytest 

def test_list_is_created():
   jobs = Tracker()
   assert jobs.todo() == []

def test_add_to_list():
    jobs = Tracker()
    jobs.add_task("first")
    assert jobs.todo() == ["first"]

def test_add_several_to_list():
    jobs = Tracker()
    jobs.add_task("first")
    jobs.add_task("second")
    assert jobs.todo() ==["first", "second"]

def test_complete_task():
    jobs = Tracker()
    jobs.add_task("first")
    jobs.add_task("second")
    jobs.complete_task("first")
    assert jobs.todo() == ["second"]

def test_add_empty_task():
    jobs = Tracker()
    with pytest.raises(Exception) as e:
        jobs.add_task("") 
    assert str(e.value) == "Don't be lazy!"

def test_complete_unrecognised_task():
    jobs = Tracker()
    jobs.add_task("first")
    with pytest.raises(Exception) as e:
        jobs.complete_task("second") 
    assert str(e.value) == "Not on list."

```