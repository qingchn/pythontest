#!/usr/bin/python
# -*- coding: utf-8 -*-

strs = "这是中文"
unis = "这也是中文".decode("utf8")

print unis

print strs[0:2]
print unis[0:2].encode('gbk')

print len(strs)
print len(unis)