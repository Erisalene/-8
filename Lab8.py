students = {
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
#Виконував Давиденко Федір ІН-33
def Print(students):
    for i in students:

        print("Оцінки ", i, " - ", students[i])
        #Виконував Давиденко Федір ІН-33
def add(students, key, grade):
    if key in students:
        print(f"Увага: запис '{key}' вже існує. Оновлюємо оцінки.")
    else:
        print(f"Додаємо нового учня: {key}")
    #Виконував Давиденко Федір ІН-33
    students[key] = grade
    print(f"Запис для '{key}' додано/оновлено успішно.")
def Del(students, key):

    del students[key]

    print("Видалено", key, ".")
    #Виконував Давиденко Федір ІН-33
def print_sort(students):

    students = {k: students[k] for k in sorted(students)}

    print("Відсортований словник: ")

    for i in students:

        print("Оцінки ", i, " - ", students[i]) 
        #Виконував Давиденко Федір ІН-33    
def show_max(students):
    max_student = max(students.items(), key=lambda x: sum(x[1]))
    print("Найвища сума оцінок у студента:", max_student[0], "—", sum(max_student[1]))
#Виконував Давиденко Федір ІН-33
def show_min(students):
    min_student = min(students.items(), key=lambda x: sum(x[1]))
    print("Найнижча сума оцінок у студента:", min_student[0], "—", sum(min_student[1])) 
    #Виконував Давиденко Федір ІН-33
def menu():
    while True:
        print("\n--- МЕНЮ ---")
        print("1 - Вивести всі записи словника")
        print("2 - Додати новий запис")
        print("3 - Видалити запис")
        print("4 - Переглянути словник за відсортованими ключами")
        print("5 - Учень з найбільшою сумою оцінок")
        print("6 - Учень з найменшою сумою оцінок")
        print("0 - Вийти з програми")

        choice = input("Введіть номер команди: ")

        if choice == "1":
            Print(students)
        elif choice == "2":
            key = input("Введіть імʼя_прізвище (англійською, без пробілів): ")
            grades = list(map(int, input("Введіть оцінки через пробіл: ").split()))
            add(students, key, grades)
        elif choice == "3":
            key = input("Введіть імʼя_прізвище для видалення: ")
            Del(students, key)
        elif choice == "4":
            print_sort(students)
        elif choice == "5":
            show_max(students)
        elif choice == "6":
            show_min(students)
        elif choice == "0":
            print("Вихід з програми...")
            break
        else:
            print("Невірна команда. Спробуйте ще раз.")
#Виконував Давиденко Федір ІН-33
menu()
