def greeting(name):
    print("Hello", name)
# def functionname():
# variable created inside function can be used inside that function. This is called local scope.
# input_name varaible used in global scope


def greeting2():
    print("Hello", input_name)


# Man Program
input_name = input('Enter your name: ')
greeting(input_name)
print('Thanks')


def addition(a, b):  # returns sum of 2 numbers
    return a + b


def main():  # function does'nt return anything
    print(addition(10, 15))


main()
