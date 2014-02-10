#!/usr/bin/env python
cities = {'CA': 'San Francisco', 'MI': 'Detroit','FL':'Jacksonville'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'


#this line print cities
print  cities

def find_city(themap,state):
    if state in themap:
        return themap[state]
    else:
        return "Not found"


#ok pay attention!

#cities['__find'] = find_city

while True:
    print "State? (ENTER to quit)",
    state = raw_input("> ")
    if not state: break
    city_found = find_city(cities,state)
    print city_found
