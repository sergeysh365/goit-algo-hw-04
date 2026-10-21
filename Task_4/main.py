# Напишіть консольного бота помічника, який розпізнаватиме команди, що вводяться з клавіатури, та буде відповідати згідно із введеною командою.

# Парсер команд. Частина, яка відповідає за розбір введених користувачем рядків, виділення з рядка ключових слів та модифікаторів команд.
def parse_input(user_input): # функція parse_input(user_input) яка приймає рядок вводу користувача user_input
    cmd, *args = user_input.split() # Рядок коду cmd, *args = user_input.split() розділяє рядок на слова. Перше слово зберігається у змінній cmd, а решта зберігається у списку args завдяки оператору розпакування *.
    cmd = cmd.strip().lower() # рядок коду cmd = cmd.strip().lower() видаляє зайві пробіли навколо команди та перетворює її на нижній регістр.
    return cmd, *args

# Функції-обробники команд - набір функцій, які ще називають handler, вони відповідають за безпосереднє виконання команд.

def add_contact(args, contacts): # Функція add_contact призначена для додавання нового контакту до словника контактів.
    name, phone = args # Всередині функції, два елементи зі списку args розпаковуються в змінні name та phone.
    contacts[name] = phone # Функція далі додає пару ключ-значення до словника контактів, використовуючи ім'я як ключ і телефонний номер як значення contacts[name] = phone.
    return "Contact added." # Функція add_contact повертає рядок, що підтверджує успішне додавання контакту: "Contact added.".

def change_contact(args, contacts): # Функція для зміни існуючого контакту
    name, phone = args
    # Перевіряємо, чи існує вже такий контакт у словнику
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return f"Error: Contact '{name}' not found."


def show_phone(name, contacts): # Функція для відображення номеру телефону конкретного контакту
    if name in contacts:
        return contacts[name]
    else:
        return f"Error: Contact '{name}' not found."


def show_all(contacts): # Функція для відображення всіх збережених контактів
    if not contacts:
        return "No contacts saved yet."

    # Формуємо красивий рядок зі списком усіх контактів
    result = "All contacts:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()


def main():
    contacts = {} # додали словник з контактами contacts = {} всередину функції main
    print("Welcome to the assistant bot!")
    # Цикл запит-відповідь. Ця частина застосунку відповідає за отримання від користувача даних та повернення користувачеві відповіді від функції - handler-а.
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            if args:  # Перевіряємо, чи користувач взагалі ввів ім'я
                name = args[0]  # Дістаємо перший елемент зі списку args
                print(show_phone(name, contacts))
            else:
                print("Error: Please provide a contact name.")
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()