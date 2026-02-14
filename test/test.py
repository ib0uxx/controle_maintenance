import unittest
from src import main 

def test_add():
    main.tasks = []
    main.add_task()
    assert len(main.tasks) == 1

def test_list():
    main.tasks = []
    main.add_task()
    main.add_task()
    assert len(main.tasks) == 2

def test_mark_completed():
    main.tasks = []
    main.add_task()
    main.mark_task_completed()
    assert main.tasks[0].completed == True


