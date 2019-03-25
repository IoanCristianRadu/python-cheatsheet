# Scalar types

# int
print(10)
print("int(3.5): ", int(3.5))
print("int(-3.5): ", int(-3.5))
print("int(\"496\"): ", int("496"))

print("Convert 10000 in base 3: ", int("10000", 3))
print("Binary: ", 0b10)
print("Octal: ", 0o10)
print("Hexadecimal: ", 0x10)

# float
float1 = 3.125
float2 = 3e8
float3 = float(7)
float4 = float("1.618")
float5 = 1.616e-35

# None
a = None
print("a is None: ", a is None)

# Bool: True / False
print("bool(0): ", bool(0))  # Falsy
print("bool(42): ", bool(42))  # Truthy
print("bool(-5): ", bool(-5))  # Truthy

# Testing
my_name = "Cristian"
my_age = 23

print("I am {0}, and I am {1} years old".format(my_name, my_age))
print(f"I am {my_name}, and I am {my_age} years old")

a = True
b = False
c = None

answer = 42
pi = 3.14159

print("\nFloat to int")
print(int(pi))

print(set([1, 1, 2, 2, 2, 3, 4, 5, 5, 5]))

""" A tuple is a collection which is ordered and unchangeable. 
    In Python tuples are written with round brackets. """
my_tuple = ("cherry", "apple", "banana")
print(my_tuple)

notTuple = ["b", "a", "c"]
print(notTuple)
