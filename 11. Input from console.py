students = []


def add_students():
    while True:
        name = input("Enter student name: ")
        id = int(input("Enter student id: "))
        student = {"name": name, "id": id}
        students.append(student)
        print(students)
        continue_flag = input("Do you wish to add more? y/n: ")
        if continue_flag == "n":
            break


add_students()
