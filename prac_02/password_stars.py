def main():
    min_length = 8
    password = get_password(min_length)
    print_asterisks(password)


def print_asterisks(password):
    print('*' * len(password))


def get_password(min_length):
    password = input("Password: ")
    while len(password) < min_length:
        print("Your password must be at least {} characters long.".format(min_length))
        password = input("Password: ")
    return password


main()