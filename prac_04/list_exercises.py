usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
             'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
             'bob']

def main():
    numbers = []
    get_numbers(numbers)
    #print(numbers)
    display_numbers(numbers)
    check_username()


def check_username():
    username = input('Enter your username: ')
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


def get_numbers(numbers):
    for i in range(5):
        number = int(input('Enter a number: '))
        numbers.append(number)


def display_numbers(numbers):
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


main()