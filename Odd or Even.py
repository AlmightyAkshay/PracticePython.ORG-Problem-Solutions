# -*- coding: utf-8 -*-
"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""

print('=====Program To Check Odd or Even Number=====')
user_inp = int(input('Please enter any integer number.'))

if user_inp % 2 == 0:
    if user_inp % 4 == 0:
        print('Number '+str(user_inp)+' is Even as well as divisible by 4.')
    else:
        print('Number '+str(user_inp)+' is Even')
else:
    print('Number '+str(user_inp)+' is Odd')

num = int(input('Enter the Divident Number.'))
check = int(input('Enter the Divisor Number.'))
if num % check == 0:
    print('Number '+str(num)+' is divisible by '+str(check))
else:
    print('Number '+str(num)+' is not divisible by '+str(check))