def var_args(name, *args):
    print(name)
    print(args)


var_args("I", "have", "infinite", "arguments")


def var_kwargs(name, **kwargs):
    print(name)
    print(kwargs["description"], kwargs["feedback"])


var_kwargs("I", description="Love python", feedback=10)

students = []


def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)


def print_students_in_one_line():
    for student in students:
        print(student, end=" | ")


def get_student(index):
    return students[index]
