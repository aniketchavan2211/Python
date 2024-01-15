#!/usr/bin/env python

num1 = float(input('Enter 1st number: '))
operation = input('Enter operation [+,-,*,/,%]: ')
num2 = float(input('Enter 2nd number: '))

if operation == '+':
  print(num1 + num2)

elif operation == '-':
  print(num1 - num2)

elif operation == '*':
  print(num1 * num2)

elif operation == '/':
  print(num1 / num2)

elif operation == '%':
  print(num1 % num2)

else:
  print('Invalid Input')
