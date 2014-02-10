#!/usr/bin/env python
#-*- coding:utf-8 -*-
def add_factorial(n):
    empty_list=[]           #声明一个空列表，存各个阶乘的结果，方便这些结果相加
    for i in map(lambda x:x+1,range(n)):    #用传进来的变量(n)来生成一个列表，用map让列表都+1，eg：range(5) => [1,2,3,4,5]
        a=reduce(lambda x,y:x*y,map(lambda x:x+1,range(i)))   #生成阶乘，用map去掉列表中的0
        empty_list.append(a)            #把阶乘结果append到空的列表中
    return empty_list
if __name__ == '__main__':
    import sys

    try:
        n = input("Enter a Number(int) : ")
        result=add_factorial(n)   #传入变量
        print reduce(lambda x,y:x+y,result)      #阶乘结果相加
    except (NameError,TypeError):
        print "That's not a Number!"
#(二)
#    result = add_factorial(int(sys.argv[1]))   #传入变量
#    print reduce(lambda x,y:x+y,result)      #阶乘结果相加




