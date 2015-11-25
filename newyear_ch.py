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
    lucker = '%s \n' %namelist[randint(0,len(namelist)-1)]
    action = raw_input('Enter')
    if lucker == str(action):
        print "OK ,The lucker is %s" %(lucker)
        break
    else:
        continue


