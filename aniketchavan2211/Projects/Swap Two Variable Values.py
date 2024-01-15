#!/usr/bin/env python

# Take User input
x = input("Enter value of x: ")
y = input("Enter value of y: ")

# (Using 3rd Variable)
# temp = x

# x = y
# print ("The value of x is: ", x)

# y = temp
# print ("The value of y is: ", y)

# (Without using 3rd Variable)
x,y = y,x
print("The value of x is", x)
print("The value of y is", y)

