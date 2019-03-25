number = 5
if number == 5:
    print("Number is 5")
else:
    print("Number is NOT 5")

if number == 5:
    print("Number is 5")
elif number > 5:
    print("Number is greater than 5")
else:
    print("Number is smaller than 5")

if number != 4:
    print("Number is not 4")

graduate = False
if not graduate:
    print("Oh, you are still a student!")

text = "Python"
if text:
    print("Text is truthy")

if text and not graduate:
    print("Text and not graduate!")

none = None
if text or none:
    print("Text or none")

a = 1
b = 2
print("bigger" if a > b else "smaller")
