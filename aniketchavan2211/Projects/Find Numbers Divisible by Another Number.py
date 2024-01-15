#!/usr/bin/env python

# Using For loops

div = int(input('Number divisble by: '))

# print ('The numbers divisible by 13 are: ')
# for i in range(1, 100):
#   if i % div == 0:
#     print(i)


# Using Lambda Function and filter()

l = [23, 17, 83, 39, 99, 36, 89, 26]

result = list(filter(lambda x : x % div == 0, l))

print('All numbers: ', l)
print('The numbers divible by',div, 'are: ', result)
