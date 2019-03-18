student_names = ["Cristian", "Victor", "Jessica"]

for name in student_names:
    print("Student name is: {0}".format(name))

print("\nRANGE PRINTED ON THE SAME LINE")
for index in range(3):
    print("Value of X is {0}".format(index), end=" | ")

print("\nRANGE WITH START, STOP")
for index in range(5, 7):
    print("Value of index is {0}".format(index))

print("\nRANGE WITH START,STOP,INCREMENT")
for index in range(5, 10, 2):
    print("Value of index is {0}".format(index))
