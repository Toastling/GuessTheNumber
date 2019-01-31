#!/usr/bin/env python

import random


currentroll = random.randint(1, int(10))
MadeCorrectGuess=False
while not MadeCorrectGuess:
    NumberRange = raw_input("I'm thinking of a number between 1 and 10. Guess the number.") 
    if int(NumberRange)== currentroll:
        MadeCorrectGuess=True
        print "Yes. That is correct."
    elif int(NumberRange)<currentroll:
        print "Nope. Go bigger."
    elif int(NumberRange)>currentroll:
        print "Nope. Go smaller."