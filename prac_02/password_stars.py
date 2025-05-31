def main():
    minimum_length = 8
    password = get_password(minimum_length)
    print_asterisks(password)


def print_asterisks(password):
    print('*' * len(password))


def get_password(minimum_length):
    password = input("Password: ")
    while len(password) < minimum_length:
        print("Your password must be at least {} characters long.".format(minimum_length))
        password = input("Password: ")
    return password


main()