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