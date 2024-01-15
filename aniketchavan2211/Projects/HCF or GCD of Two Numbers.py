#!/usr/bin/env python

# HCF - Hightest Common Factor
# GCD - Greater Common Divider

def findHCF(x, y):

  if x > y:
    smaller = y

  else:
    smaller = x

  for i in range(1, smaller + 1):
    if ((x % i == 0) and (y % i  == 0)):
      hcf = i

  return hcf

x = int(input('Enter x value: '))
y = int(input('Enter y value: '))


print('The HCF/GCD of the given two numbers is', findHCF(12, 30))
