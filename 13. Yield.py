"""Yield is a keyword that is used like return, except the function will return a generator
when you call the function, the code you have written in the function body does not run. The function only returns the generator object"""


def createGenerator():
    my_list = range(3)
    for i in my_list:
        yield i * i


my_generator = createGenerator()
print(my_generator)

for i in my_generator:
    print(i)
