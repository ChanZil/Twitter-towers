import math


def rectangle(length, height):
    if length == height or abs(length - height) > 5:
        rectangle_area = length * height
        print("The area of the rectangle is: " + rectangle_area)
    else:
        rectangle_scope = length * 2 + height * 2
        print("The scope of the rectangle is: " + rectangle_scope)


def triangle(length, height):
    triangle_option = input()
    match triangle_option:
        case '1':
            triangle_scope(length, height)
        case '2':
            if length % 2 == 0 or length > height * 2:
                print("2")
            else:
                print_triangle(length, height)
        case _:
            print("invalid choice")


def triangle_scope(length, height):
    side = math.sqrt(height ** 2 + (length / 2) ** 2)
    scope = side * 2 + length
    print("The scope of the triangle is: " + scope)


def print_triangle(length, height):
    print("triangle")