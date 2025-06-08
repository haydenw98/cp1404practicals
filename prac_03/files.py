#1
out_file = open("name.txt", "w")
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()

#2
in_file = open("name.txt", "r")
print(f"Hi {in_file.read().strip()}!")
in_file.close()

#3
with open("numbers.txt", "r") as numbers_file:
    first_number = int(numbers_file.readline())
    second_number = int(numbers_file.readline())
    print(first_number + second_number)

#4
with open("numbers.txt", "r") as numbers_file:
    total = 0
    for line in numbers_file:
        total += int(line)
    print(total)
