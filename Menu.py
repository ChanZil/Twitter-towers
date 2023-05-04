import functions


def main():
    while True:
        user_action = input("Please select one of the options")
        match user_action:
            case '1':
                print("1")
            case '2':
                print("2")
            case '3':
                break
            case _:
                print("other")


if __name__ == '__main__':
    main()

