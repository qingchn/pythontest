#/usr/local/env python
''' for new year choice name
    version 1.0
    author wangchanglin
'''


from sys import exit
from random import randint


namelist = ['a','b','c','d','e','f','g']

while True:
    print "OK,Let's go choice the year lucker"
    print '%s \n' %namelist[randint(0,len(namelist)-1)]
    action = raw_input('Enter')


