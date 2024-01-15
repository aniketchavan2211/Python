#!/usr/bin/env python

factorial = 1
num = int(input('Enter a number: '))

if num < 0:
  print('Fcatorial of 0 does not exist')

if num == 0:
  print('Factorial of 0 is', 1)

if num > 0:
  for i in range (1, num + 1):
    factorial = factorial * i
print('The Factorial of the given number is', factorial)
