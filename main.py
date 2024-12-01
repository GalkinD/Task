from task_manager import TaskManager

def main():
    manager = TaskManager("data.json")

    while True:
        print("\nМеню:")
        print("1. Добавить задачу")
        print("2. Редактировать задачу")
        print("3. Удалить задачу")
        print("4. Просмотреть задачи")
        print("5. Отметить задачу как выполненную")
        print("6. Поиск задач")
        print("0. Выход")

        choice = input("Выберите действие: ")
        if choice == "1":
            title = input("Название: ")
            description = input("Описание: ")
            category = input("Категория: ")
            due_date = input("Срок выполнения (ГГГГ-ММ-ДД): ")
            priority = input("Приоритет (низкий/средний/высокий): ")
            manager.add_task(title, description, category, due_date, priority)
        elif choice == "2":
            task_id = int(input("ID задачи: "))
            title = input("Новое название (или оставьте пустым): ") or None
            description = input("Новое описание (или оставьте пустым): ") or None
            manager.edit_task(task_id, title=title, description=description)
        elif choice == "3":
            task_id = int(input("ID задачи: "))
            manager.delete_task(task_id)
        elif choice == "4":
            for task in manager.tasks:
                print(task.to_dict())
        elif choice == "5":
            task_id = int(input("ID задачи: "))
            manager.mark_task_as_done(task_id)
        elif choice == "6":
            keyword = input("Ключевое слово (или оставьте пустым): ") or None
            results = manager.search_tasks(keyword=keyword)
            for task in results:
                print(task.to_dict())
        elif choice == "0":
            break

if __name__ == "__main__":
    main()
