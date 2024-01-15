#!/usr/bin/env python

def ConvertBinary(n):
  if n > 1:
    ConvertBinary(n // 2)
  print (n  % 2,end = '')

n = int(input('Enter a number: '))

print ('The binary of given number is: ' )
ConvertBinary(n)
print('')
