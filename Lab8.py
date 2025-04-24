# Дані
students_grades = {
    "Vitaly_Prikhodko": [12, 10, 9, 10, 5, 7, 8, 5, 12, 10], 
    "Dmytro_Kropyvnytskyi": [12, 10, 9, 5, 6, 7, 4, 3, 12, 4],
    "Mikhail_Romanenko": [12, 3, 4, 6, 5, 5, 3, 7, 5, 4], 
    "Maxim_Derizemlya": [12, 4, 10, 7, 5, 8, 3, 3, 5, 7],
    "Victoria_Zhuk": [10, 10, 10, 9, 10, 9, 10, 8, 7, 12],
    "Andrey_Kuryanov": [5, 6, 7, 5, 4, 7, 5, 4, 4, 8], 
    "Oksana_Dubovets": [7, 8, 5, 8, 8, 9, 8, 7, 7, 10], 
    "Nikita_Stroganov": [6, 7, 8, 9, 10, 10, 10, 10, 10, 9],
    "Karina_Nikolaenko": [2, 3, 5, 4, 5, 4, 3, 3, 5, 8], 
    "Eugenia_Dron": [12, 12, 12, 10, 10, 9, 8, 9, 9, 8]
}

students_info = {
    "Vitaly_Prikhodko":["IN-33","Informational technologies"],
    "Dmytro_Kropyvnytskyi": ["IN-34","Social science"],
    "Mikhail_Romanenko": ["IN-33","Social science"], 
    "Maxim_Derizemlya": ["IN-33","Social science"],
    "Victoria_Zhuk": ["IN-34","Physics"],
    "Andrey_Kuryanov": ["IN-34","Informational technologies"], 
    "Oksana_Dubovets": ["IN-34","Informational technologies"], 
    "Nikita_Stroganov": ["IN-33","Physics"],
    "Karina_Nikolaenko": ["IN-33","Informational technologies"], 
    "Eugenia_Dron": ["IN-33","Physics"]
}

# Функції
def Print(students_info):
    for student, info in students_info.items():
        print(f"{student}: Група — {info[0]}, Курс — {info[1]}")

def add(students_grades, students_info, key, grades, group, course):
    students_grades[key] = grades
    students_info[key] = [group, course]
    print(f"Додано/оновлено запис для '{key}'.")

def Del(students_grades, students_info, key):
    if key in students_grades:
        del students_grades[key]
        del students_info[key]
        print(f"Видалено {key}.")
    else:
        print(f"Учень '{key}' не знайдений.")

def print_sort(students_grades):
    sorted_students = dict(sorted(students_grades.items()))
    for student, grades in sorted_students.items():
        print(f"{student}: {grades}")

def show_max(students_grades):
    max_student = max(students_grades.items(), key=lambda x: sum(x[1]))
    print(f"Найвища сума оцінок: {max_student[0]} — {sum(max_student[1])}")

def show_min(students_grades):
    min_student = min(students_grades.items(), key=lambda x: sum(x[1]))
    print(f"Найнижча сума оцінок: {min_student[0]} — {sum(min_student[1])}")

# Меню
def menu():
    while True:
        print("\n--- МЕНЮ ---")
        print("1 - Вивести інформацію про студентів")
        print("2 - Додати нового студента")
        print("3 - Видалити студента")
        print("4 - Переглянути оцінки за алфавітом")
        print("5 - Студент з найбільшою сумою оцінок")
        print("6 - Студент з найменшою сумою оцінок")
        print("0 - Вийти з програми")

        choice = input("Введіть номер команди: ")

        if choice == "1":
            Print(students_info)
        elif choice == "2":
            key = input("Введіть імʼя_прізвище (без пробілів): ")
            grades_input = input("Введіть оцінки через пробіл: ")
            grades = list(map(int, grades_input.split()))
            group = input("Введіть назву групи: ")
            course = input("Введіть назву курсу: ")
            add(students_grades, students_info, key, grades, group, course)
        elif choice == "3":
            key = input("Введіть імʼя_прізвище для видалення: ")
            Del(students_grades, students_info, key)
        elif choice == "4":
            print_sort(students_grades)
        elif choice == "5":
            show_max(students_grades)
        elif choice == "6":
            show_min(students_grades)
        elif choice == "0":
            print("Вихід з програми...")
            break
        else:
            print("Невірна команда. Спробуйте ще раз.")

# Виконував Давиденко Федір ІН-33
menu()
