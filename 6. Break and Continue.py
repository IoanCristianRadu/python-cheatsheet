student_names = ["Cristian", "Victor", "Jessica"]
student = "Victor"

print("\nBREAK")
for name in student_names:
    print(name)
    if name == student:
        print(f"Found {student}!")
        break

print("\nCONTINUE")
for name in student_names:
    if name == student:
        continue
        print(f"Found {student}!")
    print(name)
