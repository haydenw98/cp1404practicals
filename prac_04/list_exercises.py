def main():
    numbers = []
    get_numbers(numbers)
    #print(numbers)
    display_numbers(numbers)


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