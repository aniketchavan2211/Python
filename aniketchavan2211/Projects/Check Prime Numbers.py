#!/usr/bin/env python

num = int(input('Enter a number: '))

if num ==1:
  print(num, 'is not a prime number')

if num > 1:
  for i in range(2, num):
    if num % i == 0:
      print('it is not a prime number')
      break

  else:
    print('It is a prime number')
