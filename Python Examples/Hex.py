#!/usr/bin/env python
"""
Finding if a given value is hexadecimal
"""

__author__ = """Sudershan Malpani (sudershan.malpani@gmail.com)"""

import re

val=raw_input("Enter any value: ")
p=re.search("\A0x",val)
if(p):
    m=re.split("x",val)
    if((len(m))>2):
        print "value not Hex"
    else:
        e=re.findall("[0-9a-fA-F]",m[1])
        if(len(m[1])>len(e)):
            print "value not Hex"
        else:
            print "Value is Hex!!"
else:
    m=re.findall("[0-9a-fA-F]",val)
    if(len(val)>len(m)):
        print "value not Hex"
    else:
        print "Value is Hex!!"

    

