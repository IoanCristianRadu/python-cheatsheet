student = {
    "name": "Mark",
    "student_id": 156,
    "feedback": None
}

print(student["name"])
print(student.get("last_name", "print me if last_name is not found"))
print(student.keys())
print(student.values())

print("\nDELETING KEY")
del student["name"]
print(student.keys())
print(student.values())

print("\nVECTOR OF DICTIONARIES")
all_students = [
    {"name": "Mark", "student_id": 156},
    {"name": "Jessica", "student_id": 177},
    {"name": "Kevin", "student_id": 198}
]
print(all_students[0].values())
print(all_students[1]["name"])

print("\nManually add to a dictionary")
dictionary = {}
dictionary["name"] = "charlie"
dictionary["age"] = 34

print(dictionary)