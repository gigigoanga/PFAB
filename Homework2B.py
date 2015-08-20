#!/usr/bin/env python
 
 
cost = input("What is the cost of the item?")
tax = input("What is the sales tax rate (expressed as 0.xx)?")
 
print "The full price of the item is $", cost*tax+cost
