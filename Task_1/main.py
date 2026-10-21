from pathlib import Path
import sys

def total_salary(path: str) -> tuple[float, float]:
    """
    Функція аналізує файл із зарплатами розробників.
    Функція повертає кортеж: (загальна_сума, середня_зарплата).
    """
    total = 0.0
    count = 0

    try:
        # Використання менеджеру контексту для безпечного відкриття файлу
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                if not line:
                    continue  # Пропускаємо порожні рядки
                
                try:
                    # Розділення рядка за комою
                    name, salary_str = line.split(',')
                    # Конвертація зарплати у число та додавання до загальної суми
                    total += float(salary_str)
                    count += 1
                except ValueError:
                    print(f"Попередження: Некоректний формат даних у рядку: '{line}'")
                    continue

        # Якщо файл був порожнім або без коректних даних
        if count == 0:
            return 0.0, 0.0

        # Обчислюємо середню заробітну плату
        average = total / count
        return total, average

    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return 0.0, 0.0
    except Exception as e:
        print(f"Сталася непередбачена помилка при роботі з файлом: {e}")
        return 0.0, 0.0


if __name__ == "__main__":
    # Перевірка наявності шляху до файлу sys.argv[1]
    if len(sys.argv) < 2:
        print("Помилка: Ви не вказали шлях до файлу!")
        print("Використання: python script.py <шлях_до_файлу>")
        sys.exit(1)

    # Отримання шляху з першого аргументу командного рядка
    file_path = sys.argv[1]

    # Виклик функції та виведення результату
    total, average = total_salary(file_path)
    
    print(f"Загальна сума заробітної плати: {total}")
    print(f"Середня заробітна плата: {average}")