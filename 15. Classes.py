students = []


class Student:
    school_name = "Stockholm University"

    def __init__(self, name, student_id=000):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def print_name(self):
        print(self.name.capitalize())

    def get_school_name(self):
        return self.school_name


student = Student("Michael")
student.print_name()
print(student)
print(Student.school_name)
