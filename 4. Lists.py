student_names = ["Cristian", "Victor", "Jessica"]

"""Modifying a list item"""
student_names[0] = "Cristi"
print(student_names)

"""Appending items"""
student_names.append("Oscar")
print(student_names)

"""Finding if an item is in the list"""
print("Cristi" in student_names)
print(len(student_names))

"""Appending different variable types"""
student_names.append(12)
print(student_names)

"""Deleting items"""
del student_names[4]
print(student_names)

"""Ignoring the first and last element"""
print(student_names[1:-1])

"""Element ranges"""
print(student_names[1:4])
