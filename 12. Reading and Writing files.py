students = []


def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save file")


def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            student = student[:-1]
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")


def add_student(student):
    students.append({"name": student})


def add_students_from_console():
    while True:
        name = input("Enter student name: ")
        student = {"name": name}
        students.append(student)
        save_file(student["name"])
        print(students)
        continue_flag = input("Do you wish to add more? y/n: ")
        if continue_flag == "n":
            break


read_file()
print("Current students:", students)
add_students_from_console()
