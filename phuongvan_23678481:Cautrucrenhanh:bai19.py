#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 15:07:38 2024

@author: nguyenthiphuongvan2005
"""

a= int(input("Nhập số nguyên a: "))
b= int(input("Nhấp số nguyên b: "))
c= int(input("Nhập số nguyên c: "))
d= int(input("Nhập số nguyên d: "))

if a<b and a<c and a<d:
    print("số nhỏ nhất là: ", a)
    
elif b<a and b<c and b<d:
    print("số nhỏ nhất là: ", b)
    
elif c<a and c<b and c<d:
    print("số nhỏ nhất là: ", c)
    
else: 
    print("số nhỏ nhất là: ", d)
    


