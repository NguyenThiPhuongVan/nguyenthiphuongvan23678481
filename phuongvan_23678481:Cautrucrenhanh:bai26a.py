#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:26:22 2024

@author: nguyenthiphuongvan2005
"""


a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))

if a > b:
    a, b = b, a  
if a > c:
    a, c = c, a  
if b > c:
    b, c = c, b  

print("Các số theo hứ tự tăng dần: ", a, b, c)

