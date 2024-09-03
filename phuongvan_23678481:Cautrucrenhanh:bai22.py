#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:36:15 2024

@author: nguyenthiphuongvan2005
"""

a= float(input("Nhập số hệ số a: "))
b= float(input("Nhập số hệ số b: "))

if a==0 and b==0:
    print("phương trình vô số nghiệm")
elif a==0 and b!=0:
    print("phương trình vô nghiệm")
elif a!=0 and b==0:
    print ("phương trình vô nghiệm")
else: 
    x= -b/a 
    print ("phương trình có  x= ", x)
    
