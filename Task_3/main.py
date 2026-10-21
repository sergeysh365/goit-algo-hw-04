import sys
from pathlib import Path
from colorama import Fore, Style, init

# Ініціалізація colorama для підтримки кольорів у всіх ОС
init(autoreset=True)

def parse_folder(path: Path) -> None:
    try:
        # Рекурсивний обхід елементів (відсортований для красивого виведення)
        for element in sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower())):
            # Рахуємо рівень відносно БАТЬКІВСЬКОЇ папки початкового шляху,
            # щоб перший рівень вкладеності вже мав відступ у 4 пробіли
            level = len(element.relative_to(parent_folder_path.parent).parts) - 1
            indent = "    " * level

            if element.is_dir():
                print(f"{indent}{Fore.RED}{element.name}/")
                parse_folder(element)  # Приймає строго ОДИН параметр
            elif element.is_file():
                print(f"{indent}{Fore.GREEN}{element.name}")

    except PermissionError:
        print(f"{Fore.YELLOW}Помилка доступу до директорії: {path.name}")
    except Exception as e:
        print(f"{Fore.RED}Сталася помилка при обході: {e}")

def main():
    # Робимо змінну глобальною, щоб функція parse_folder могла рахувати рівні від неї
    global parent_folder_path

    # Перевірка отримання аргументу командного рядка
    if len(sys.argv) < 2:
        print(f"{Fore.YELLOW}Будь ласка, вкажіть шлях до директорії.")
        sys.exit(1)

    parent_folder_path = Path(sys.argv[1])

    # Перевірка та обробка помилок шляху
    if not parent_folder_path.exists():
        print(f"{Fore.RED}Помилка: Шлях '{parent_folder_path}' не існує.")
        sys.exit(1)

    if not parent_folder_path.is_dir():
        print(f"{Fore.RED}Помилка: Шлях '{parent_folder_path}' не є директорією.")
        sys.exit(1)

    # Виводимо назву кореневої папки, як на скріншоті
    print(f"{Fore.BLUE}{parent_folder_path.name}/")

    # Запуск рекурсії
    parse_folder(parent_folder_path)

if __name__ == "__main__":
    main()