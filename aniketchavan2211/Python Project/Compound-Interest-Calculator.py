#!/bin/python 

account = 100 
interest_rate = 0.004
years = 3

print (f"Initial amount:{account}")

accrued_interest = account * interest_rate

counter = 1
while counter <= years:
  account += accrued_interest
  print (f"year{counter}:{account}")
  counter += 1

