class Student:
    school_name = "Stockholm University"

    def __init__(self, name, student_id=000):
        self.name = name
        self.student_id = student_id

    def __str__(self):
        return "Student " + self.name

    def print_name(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name


class HighSchoolStudent(Student):
    school_name = "Stockholm Highschool"

    def get_school_name(self):
        return self.school_name

    def print_name(self):
        return super().print_name() + "-HS"
