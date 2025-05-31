min_length = 8
password = input("Password: ")
while len(password) < min_length:
    print("Your password must be at least {} characters long.".format(min_length))
    password = input("Password: ")
print('*' * len(password))