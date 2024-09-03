#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:16:47 2024

@author: nguyenthiphuongvan2005
"""

a = int(input("Nhập giờ: "))
b = int(input("Nhập phút: "))
c = int(input("Nhập giây: "))
if a<=24: 
    print("Giờ hợp lệ.")
else:
    print("Giờ không hợp lệ.")
if b<=60:
    print("Phút hợp lệ.")
else:
    print("Phút không hợp lệ.")
if c<=60:
    print("Giây hợp lệ.")
else:
    print("Giây không hợp lệ.")
    
