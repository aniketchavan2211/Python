#!/bin/python

# Celsuis
def celsuis():
	C = int(input("Enter Temp in Celsius: "))
	F = (C * 1.8) + 32
	print ("The Converted value is ", str(F) , "°F")

# Fahrenheit
def fahrenheit():
	F = int(input("Enter Temp in Fahrenheit: "))
	C = (F - 32) * (5/9)
	print ("The Convert Value is: ",str(C), "°C")

# Selection
print ("Select Conversion : ")
print ("1) Convert Celsuis to Fahrenheit")
print ("2) Convert Fahrenhiet to Celsuis")
value = str(input("Select: "))

# if-elif-else statement
if value == str(1):
  celsuis()
elif value == str(2):
  fahrenheit()
elif value < str(1) or value > str(2):
  print ("Please enter a valid number")
elif value == str(""):
  print (" Please Enter a Number")
else:
  print ("Error")
