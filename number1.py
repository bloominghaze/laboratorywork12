import json

employees = [
    {"Surname": "Tkachenko", "Salary": 5000, "Position": "Manager", "Gender": "Male"},
    {"Surname": "Ivanov", "Salary": 7000, "Position": "Developer", "Gender": "Male"},
    {"Surname": "Petrova", "Salary": 3000, "Position": "Designer", "Gender": "Female"},
    {"Surname": "Sidorov", "Salary": 4000, "Position": "Developer", "Gender": "Male"},
    {"Surname": "Koval", "Salary": 5500, "Position": "Manager", "Gender": "Female"},
    {"Surname": "Novak", "Salary": 3500, "Position": "Designer", "Gender": "Female"},
    {"Surname": "Lysenko", "Salary": 4500, "Position": "Developer", "Gender": "Male"},
    {"Surname": "Bondar", "Salary": 2500, "Position": "Designer", "Gender": "Female"},
    {"Surname": "Shevchenko", "Salary": 6000, "Position": "Manager", "Gender": "Male"},
    {"Surname": "Rudenko", "Salary": 8000, "Position": "Developer", "Gender": "Female"}
]

with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)

def view_data():
    with open("employees.json", "r") as file:
        data = json.load(file)
        print(*data, sep='\n')

def add_employee():
    with open("employees.json", "r") as file:
        data = json.load(file)

    surname = input("Прізвище: ")
    salary = int(input("Зарплата: "))
    position = input("Посада: ")
    gender = input("Стать: ")

    data.append({"Surname": surname, "Salary": salary, "Position": position, "Gender": gender})

    with open("employees.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Новий запис додано.")

def delete_employee():
    with open("employees.json", "r") as file:
        data = json.load(file)

    surname = input("Введіть прізвище співробітника, якого потрібно видалити: ")

    updated_data = [emp for emp in data if emp["Surname"] != surname]

    if len(updated_data) == len(data):
        print("Співробітника з таким прізвищем не знайдено.")
    else:
        with open("employees.json", "w") as file:
            json.dump(updated_data, file, indent=4)
        print("Запис видалено.")

def search_employee():
    with open("employees.json", "r") as file:
        data = json.load(file)

    surname = input("Введіть прізвище для пошуку: ")

    result = [emp for emp in data if emp["Surname"] == surname]

    if result:
        print(*result, sep='\n')
    else:
        print("Співробітника з таким прізвищем не знайдено.")

def find_salary_extremes():
    with open("employees.json", "r") as file:
        data = json.load(file)

    min_salary_emp = min(data, key=lambda x: x["Salary"])
    max_salary_emp = max(data, key=lambda x: x["Salary"])

    print(f"Найменша зарплата у {min_salary_emp['Surname']}: {min_salary_emp['Salary']}")
    print(f"Найбільша зарплата у {max_salary_emp['Surname']}: {max_salary_emp['Salary']}")

    # Запис результатів у новий JSON файл
    with open("salary_extremes.json", "w") as result_file:
        json.dump({"Min Salary Employee": min_salary_emp, "Max Salary Employee": max_salary_emp}, result_file, indent=4)

def main():
    while True:
        print("\nОберіть опцію:")
        print("1 - Вивести дані")
        print("2 - Додати запис")
        print("3 - Видалити запис")
        print("4 - Пошук за прізвищем")
        print("5 - Найменша та найбільша зарплата")
        print("6 - Вийти")

        choice = input("Ваш вибір: ")

        if choice == '1':
            view_data()
        elif choice == '2':
            add_employee()
        elif choice == '3':
            delete_employee()
        elif choice == '4':
            search_employee()
        elif choice == '5':
            find_salary_extremes()
        elif choice == '6':
            print("До побачення!")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()
