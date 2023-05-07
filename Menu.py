import functions


def main():
    while True:
        user_action = input("Press 1 for rectangle tower, 2 for triangle tower or 3 to exit: ")
        match user_action:
            case '1':
                width = input("Insert the width of the rectangle tower: ")
                height = input("Insert the height of the rectangle tower: ")
                functions.rectangle(int(width), int(height))
            case '2':
                width = input("Insert the width of the triangle tower: ")
                height = input("Insert the height of the triangle tower: ")
                functions.triangle(int(width), int(height))
            case '3':
                break
            case _:
                print("Invalid choice")


if __name__ == '__main__':
    main()

