#!/bin/python3

print(50 * '-')
print("| A simple Calculator")
print(50 * '-')
print('\n')

def get_input():
    while True:
        try:
            first_number = int(input('Your first number: '))
            operator = input('Which operator (+, -, *, /): ')
            second_number = int(input('Your second number: '))
            return first_number, operator, second_number
        except ValueError:
            print("Wrong input, enter numbers only! Try again.")

def result(x, o, y):
    if o == '+':
        return x + y
    elif o == '-':
        return x - y
    elif o == '*':
        return x * y
    elif o == '/':
        return x / y
    else:
        return "Error: Unknown operator!"

first_number, operator, second_number = get_input()
print('_' * 40)
print('Rusult is:')
print(result(first_number, operator, second_number))
