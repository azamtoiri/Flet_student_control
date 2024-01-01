import os
import sys


def create_app_structure(app_name):
    # Создаем папку для приложения
    app_folder = os.path.join(os.getcwd(), app_name)

    # Проверяем, существует ли уже папка с таким именем
    if os.path.exists(app_folder):
        print(f"Ошибка: Проект с именем '{app_name}' уже существует.")
        sys.exit(1)

    os.makedirs(app_folder)

    # Создаем файл приложения
    app_file_path = os.path.join(app_folder, f"{app_name}.py")
    with open(app_file_path, 'w', encoding='utf-8') as app_file:
        app_file.write(f"# {app_name}.py - ваш код приложения здесь")

    # Создаем файл __init__.py в главной папке
    app_init_file_path = os.path.join(app_folder, '__init__.py')
    with open(app_init_file_path, 'w', encoding='utf-8'):
        pass

    # Создаем папку utils
    utils_folder = os.path.join(app_folder, 'utils')
    os.makedirs(utils_folder)

    # Создаем файл __init__.py в папке utils
    utils_init_file_path = os.path.join(utils_folder, '__init__.py')
    with open(utils_init_file_path, 'w', encoding='utf-8'):
        pass

    # Создаем папку views
    views_folder = os.path.join(app_folder, 'views')
    os.makedirs(views_folder)

    # Создаем файл __init__.py в папке views
    views_init_file_path = os.path.join(views_folder, '__init__.py')
    with open(views_init_file_path, 'w', encoding='utf-8'):
        pass

    print(f"Приложение {app_name} успешно создано.")


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] != "startapp":
        print("Использование: python main.py startapp [название приложения]")
    else:
        app_name = sys.argv[2]
        create_app_structure(app_name)
