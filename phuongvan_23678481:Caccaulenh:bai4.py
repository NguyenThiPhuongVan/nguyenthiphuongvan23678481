#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 11:34:31 2024

@author: nguyenthiphuongvan2005
"""

N = int(input("Nhập số nguyên dương có 2 chữ số: "))
if 10 <= N <= 99:
    a= N // 10
    b= N % 10
print ("Kết quả", a + b)
        