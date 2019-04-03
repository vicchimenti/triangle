import sys


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
    return 0;


def scalene(a, b, c):

