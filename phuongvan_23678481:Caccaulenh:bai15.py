#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 14:26:30 2024

@author: nguyenthiphuongvan2005
"""

a= int(input("Nhập số a: "))
b= int(input("Nhập số b: "))

s=((a**(1/2)-b**(1/2))/(a**(1/3)-b**(1/3))) - ((a**(1/2)+(a*b)**(1/3))/(a**(1/3)+b**(1/3)))

print("Ket qua la: ",s)
