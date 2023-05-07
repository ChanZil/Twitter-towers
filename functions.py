import math


def rectangle(width, height):
    """
    prints the scope or the area of a rectangle
    :param width: the width of the rectangle
    :param height: the height of the rectangle
    :return: none
    """
    if width == height or abs(width - height) > 5:
        rectangle_area = str(width * height)
        print("The area of the rectangle is: " + rectangle_area)
    else:
        rectangle_scope = str(width * 2 + height * 2)
        print("The scope of the rectangle is: " + rectangle_scope)


def triangle(width, height):
    """
    Manages the triangle options.
    :param width: the width of the triangle
    :param height: the height of the triangle
    :return: none
    """
    triangle_option = input("Press 1 for triangle scope or 2 for printing the triangle: ")
    match triangle_option:
        case '1':
            triangle_scope(width, height)
        case '2':
            if width % 2 == 0 or width > height * 2:
                print("It is not possible to print the triangle")
            else:
                print_triangle(width, height)
        case _:
            print("Invalid choice")


def triangle_scope(width, height):
    """
    Prints the scope of the triangle
    :param width:
    :param height:
    :return: none
    """
    side = math.sqrt(height ** 2 + (width / 2) ** 2)
    scope = str(side * 2 + width)
    print("The scope of the triangle is: " + scope)


def print_triangle(width, height):
    """
    Prints the triangle shape
    :param width:
    :param height:
    :return: none
    """
    i_height = 1
    i_width = 1
    lines_amount = 0
    top_lines_amount = 0
    if height > 2:
        lines_amount = int((height - 2) / int((width - 2) / 2))
        top_lines_amount = (height - 2) % int((width - 2) / 2) + lines_amount
    while i_height <= height:
        star = '*' * i_width
        num_spaces = int((width - i_width) / 2)
        space = ' ' * num_spaces
        if i_width == 1 or i_width == width:
            it = 1
        elif i_width == 3:
            it = top_lines_amount
        else:
            it = lines_amount
        for i in range(it):
            print(space + star + space)
            i_height += 1
        i_width += 2
