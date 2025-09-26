def dec_bin(number):
    storage = ""
    while(number):
        rest = number % 2
        str_rest = str(rest)
        storage += str_rest
        number = number // 2
    binary = storage[::-1]
    return binary
def dec_hex(number):
    storage = ""
    while(number):
        rest = number % 16
        if rest == 10:
            rest = 'A'
        elif rest == 11:
            rest = 'B'
        elif rest == 12:
            rest = 'C'
        elif rest == 13:
            rest = 'D'
        elif rest == 14:
            rest = 'E'
        elif rest == 15:
            rest = 'F'
        str_rest = str(rest)
        storage += str_rest
        number = number // 16
    hexadecimal = storage[::-1]
    return hexadecimal
def dec_oct(number):
    storage = ""
    while(number):
        rest = number % 8
        str_rest = str(rest)
        storage += str_rest
        number = number // 8
    octal = storage[::-1]
    return octal
try:
   decider = int(input("Enter [1] for binary, [2] for hexadecimal, [3] for octal, and [4] for all: "))
except ValueError:
    raise ValueError("Please enter only integer numbers between 1 and 4. Try again!")
if decider == 1:
    number = int(input("Enter the number to be converted: "))
    result = dec_bin(number)
    print(result)
elif decider == 2:
    number = int(input("Enter the number to be converted: "))
    result = dec_hex(number)
    print(result)
elif decider == 3:
    number = int(input("Enter the number to be converted: "))
    result = dec_oct(number)
    print(result)
elif decider == 4:
    number = int(input("Enter the number to be converted: "))
    result = dec_bin(number)
    print(result)
    result = dec_hex(number)
    print(result)
    result = dec_oct(number)
    print(result)
else:
    print(f'{decider} is not a valid option. Try again...')
