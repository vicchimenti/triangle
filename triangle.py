def input_test(a, b, c):
    if a or b or c <= 0:
        return 0
    return 1


def valid_triangle(a, b, c):
    if a+b <= c:
        return 0
    elif a+c <= b:
        return 0
    elif c+b <= a:
        return 0
    return 1


def equilateral(a, b, c):
    if a == b == c:
        return 1
    return 0


def isosceles(a, b, c):
    if a == b and a != c:
        return 1
    elif a == c and a != b:
        return 1
    elif c == b and c != a:
        return 1
    return 0


def scalene(a, b, c):
    if a != b and a != c and c != b:
        return 1
    return 0


print("Enter the dimensions of the triangle: ")
a = input("Side 1: ")
b = input("Side 2: ")
c = input("Side 3: ")

if input_test(a, b, c) == 1:
    if valid_triangle(a, b, c) == 1:
        if equilateral(a, b, c) == 1:
            print("You have an equilateral triangle")
        elif isosceles(a, b, c) == 1:
            print("You have an Isosceles Triangle")
        elif scalene(a, b, c) == 1:
            print("You have a Scalene Triangle")
        else:
            print("This is a right triangle")
    else:
        print("You did not submit a valid triangle")
else:
    print("Invalid input. Please rerun the program and enter valid positive numbers.")
