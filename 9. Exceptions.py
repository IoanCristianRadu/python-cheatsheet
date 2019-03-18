student = {
    "name": "Cristian",
    "student_id": 189,
    "feedback": None
}

try:
    last_name = student["last_name"]
except KeyError:
    print("Error found!")
finally:
    print("Finally\n")


try:
    numberString = 3 + "String"
except TypeError:
    print("Can't add a number to a string\n")


try:
    numberString = 3 + "String"
except TypeError as error:
    print("Can't add a number to a string")
    print(error)


try:
    numberString = 3 + "String"
except Exception:
    print("\nUnknown error")
