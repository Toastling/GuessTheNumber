#!/usr/bin/env python

import random


currentroll = random.randint(1, int(10))
NumberRange=-1
while int(NumberRange) != currentroll:
    NumberRange = raw_input("I'm thinking of a number between 1 and 10. Guess the number.") 
    if int(NumberRange) < currentroll:
        print "Nope. Go bigger."
    else:
        print "Nope. Go smaller."

print "Yes. That is correct."
