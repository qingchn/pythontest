#!/usr/bin/python
# -*- coding: utf-8 -*-
#


class TheObject(object):

    def __init__(self):
        self.number = 0

    def re_string(self):
        print "I will return this string"

    def add_up(self,more):
        self.number += more
        return self.number

a = TheObject()
b = TheObject()

a.re_string()
b.re_string()

print a.add_up(40)
print b.add_up(50)


class duble(object):

    def __init__(self,base):
        self.base = base

    def do_it(self,m):
        return self.base * m

x = duble(a.number)

print x.do_it(b.number)

a = lambda x:x+3

a()



