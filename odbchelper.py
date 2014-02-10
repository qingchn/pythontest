#!/usr/bin/python
# -*- coding: utf-8 -*-
def buildConnectionString(params):
    """ Build a connection string from a dictinary of parameters.
    Returns string

    """
    return ":".join(["%s=%s" %(k,v) for k, v in params.items()])

if __name__ == "__main__":
    myParams = {"server":"mpilgrium","database":"master","uid":"sa","pwd":"secrt"}
    print buildConnectionString(myParams)