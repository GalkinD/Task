import pytest
from task_manager import Task, TaskManager

@pytest.fixture
def task_manager():
    return TaskManager("test_data.json")

def test_add_task(task_manager):
    task_manager.add_task("Test Task", "Description", "Work", "2024-12-31", "High")
    assert len(task_manager.tasks) == 1
    assert task_manager.tasks[0].title == "Test Task"

def test_edit_task(task_manager):
    task_manager.add_task("Test Task", "Description", "Work", "2024-12-31", "High")
    task_manager.edit_task(1, title="Updated Task")
    assert task_manager.tasks[0].title == "Updated Task"

def test_delete_task(task_manager):
    task_manager.add_task("Test Task", "Description", "Work", "2024-12-31", "High")
    task_manager.delete_task(1)
    assert len(task_manager.tasks) == 0

def test_search_tasks(task_manager):
    task_manager.add_task("Test Task 1", "Description 1", "Work", "2024-12-31", "High")
    task_manager.add_task("Test Task 2", "Description 2", "Personal", "2024-12-30", "Medium")
    task_manager.add_task("Another Task", "Description 3", "Learning", "2024-12-29", "Low")

    # Поиск по ключевому слову
    results = task_manager.search_tasks(keyword="Test")
    assert len(results) == 2

    # Поиск по категории
    results = task_manager.search_tasks(category="Work")
    assert len(results) == 1

    # Поиск по статусу
    results = task_manager.search_tasks(status="Не выполнена")
    assert len(results) == 3

def test_mark_task_as_done(task_manager):
    task_manager.add_task("Test Task", "Description", "Work", "2024-12-31", "High")
    task_manager.mark_task_as_done(1)
    assert task_manager.tasks[0].status == "Выполнена"

def test_load_and_save_tasks(task_manager):
    task_manager.add_task("Persistent Task", "Description", "Work", "2024-12-31", "High")
    task_manager.save_tasks()

    # Создаем новый менеджер, чтобы проверить загрузку данных
    new_manager = TaskManager("test_data.json")
    assert len(new_manager.tasks) == 1
    assert new_manager.tasks[0].title == "Persistent Task"
