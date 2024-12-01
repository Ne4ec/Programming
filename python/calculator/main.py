#/bin/pyhton

print(50 * '-')
print('-' * 18 + "| Calculator  |" +  '-' * 17)
print(50 * '-')
print('\n')


while True:
    try:
        first_number = int(input('You first number: '))
        operator = input('Which operator: ')
        secend_number = int(input('You secend number: '))
    except ValueError:
        print("Wrong input, enter just a number! Try again.")

def result(x, o, y):
    if o == '+':
        result = x + y
    elif o == '-':
        return x - y
    elif o == '*':
        return x * y
    elif o == '/':
        return x / y

result_tmp = (result(first_number, operator, secend_number))

print()
