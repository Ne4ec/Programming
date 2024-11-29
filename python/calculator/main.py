#/bin/pyhton

print(53 * '-')
print('-' * 19 + "| Calculator  |" +  '-' * 19)
print(53 * '-')

first_number = int(input('You first number: '))
operator = input('Which operator: ')1
secend_number = int(input('You secend number: '))

def result(x, o, y):
    if o == '+':
        result = x + y
    elif o == '-':
        return x - y
    elif o == '*':
        return x * y
    elif o == '/':
        return x / y

print(result(firt_number, operator, secend_number)
