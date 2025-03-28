'''Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
Perform the operation based on the user's input and print the result.
Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.'''

print('')
num_1 = float(input('Enter the first number. '))
print('')
operator = input('select the operator (+, *, /, or -). ')
print('')
num_2 = float(input('Enter the second number. '))
print('')

if operator == '+':
    result = num_1 + num_2
    print(f'the sum of {num_1} and {num_2} is {result}')

elif operator == '-':
    result = num_1 - num_2
    print(f'the difference between {num_1} and {num_2} is {result}')

elif operator == '*':
    result = num_1 * num_2
    print(f'the product of {num_1} and {num_2} is {result}')

elif operator == '/':
    result = num_1 / num_2
    print(f'the quotient of {num_1} and {num_2} is {result}')

else:
    print('Please select a valid operator')

print('')