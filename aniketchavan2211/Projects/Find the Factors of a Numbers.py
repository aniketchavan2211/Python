
#!/usr/bin/env python

num = int(input('Enter a number: '))

for i in range(1, num + 1):
  if num % i == 0:
    print('Factor of', num, 'is: ',i)
