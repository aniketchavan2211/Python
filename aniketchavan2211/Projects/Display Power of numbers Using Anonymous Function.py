#!/usr/bin/env python

value = int(input('Enter the base number: '))

Power = int(input('Enter number of terms (Power denoted by n): '))

result = list(map(lambda x : value ** x, range(Power+1)))


for i in range (Power+1):
  print("The value of ",value," raised to power(n) ", i, " is ", result[i])
