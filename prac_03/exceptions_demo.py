"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError will occur when a value that cant be converted into an integer is input, ie : 4.5, abc, left blank.

2. When will a ZeroDivisionError occur?
A ZeroDivisonError will occur when the denominator is input as 0.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Checking if the input is 0 before division will do this!

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")