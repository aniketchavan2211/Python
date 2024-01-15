#!/usr/bin/env python

a = input('Enter a string: ')

rev = a[::-1]

if a == rev:
  print('\033[1;32mIt is palindrome number\033[0m')

else:
  print('\033[1;31mIt is NOT palindorme number\033[0m')
