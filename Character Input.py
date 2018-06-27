# -*- coding: utf-8 -*-

"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
Print out that many copies of the previous message on separate lines.
"""

from datetime import datetime

user_nm = str(input('Hello There! what is your name?'))
nm = ('Hello '+user_nm+' nice to meet you.')
user_age = int(input('That is great. Btw how old are you?'))
ag = ('''So you're '''+str(user_age)+' years old. And you will turn 100 years old in the year '+str((datetime.now().year-user_age)+100))

sample_nbr = int(input('Okay, Give me any number.'))

if sample_nbr > 0:
    for x in range(1,sample_nbr+1):
        print(str(nm)+'\n'+str(ag)+'\n')
else:
    print('Oops...try again.')