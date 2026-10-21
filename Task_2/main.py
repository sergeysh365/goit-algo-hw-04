from pathlib import Path
import sys

def get_cats_info(path: str) -> list[dict]:
    """
    Функція зчитує файл з інформацією про котів.
    Функція повертає список словників: {"id": "", "name": "", "age": ""}.
    """
    cats_info_list = []

    try:
        # Використання менеджеру контексту для безпечного відкриття файлу
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip() # Обов'язково прибираємо зайві пробіли та символи переносу \n
                if not line:
                    continue # Пропускаємо порожні рядки

                try:
                    # Розділення рядка за комою
                    cat_id, name, age = line.split(',')

                    # Створюємо словник безпосередньо з отриманих змінних
                    cat_data = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }
                    cats_info_list.append(cat_data)

                except ValueError:
                    print(f"Попередження: Некоректний формат даних у рядку: '{line}'")
                    continue

    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
    except Exception as e:
        print(f"Сталася непередбачена помилка при роботі з файлом: {e}")

    return cats_info_list

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Помилка: Ви не вказали шлях до файлу!")
        print("Використання: python script.py <шлях_до_файлу>")
        sys.exit(1)
    
    file_path = sys.argv[1]  # Отримання шляху з першого аргументу командного рядка
    
    cats_info = get_cats_info(file_path)
    print(cats_info)