#!/usr/bin/env python

import random

# sides = raw_input("You have a die! How many sides does it have?") 
# numrolls = raw_input("How many times would you like to roll?")
# type(sides)
# type(numrolls)
# print "Rolling die... Your results are:"
# i = 0
# total = 0
# while i < int(numrolls):
#     currentroll = random.randint(1, int(sides))
#     total = total + currentroll
#     print currentroll
#     i = i + 1
# t = raw_input("Would you like a total?")
# type(t) 
# if t.strip() == "Yes":
#     print total
# else: print ("Okay. Bye. Dumb bitch :)")

# NumberRange = raw_input("I'm thinking of a number between 1 and 10. Guess the number.") 
# numrolls = raw_input("How many times would you like to roll?")
# print "Rolling die... Your results are:"
# i = 0

#     currentroll = random.randint(1, int(10))
#     return currentroll
#     i = i + 1
# t = raw_input("Would you like a total?")
# type(t) 
# if t.strip() == "Yes":
#     print total
# else: print ("Okay. Bye. Dumb bitch :)")




currentroll = random.randint(1, int(10))
NumberRange=-1
while int(NumberRange) != currentroll:
    NumberRange = raw_input("I'm thinking of a number between 1 and 10. Guess the number.") 
    if int(NumberRange) < currentroll:
        print "Nope. Go bigger."
    else:
        print "Nope. Go smaller."

print "Yes. That is correct."
