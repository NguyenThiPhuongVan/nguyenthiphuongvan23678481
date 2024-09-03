#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:42:16 2024

@author: nguyenthiphuongvan2005
"""

import math 

A= input("Nhập hình: ")
if A== 'vuông':
    a = float(input("Nhập chiều dài cạnh của hình vuông: "))
    p = 4 * a
    s = a * a
    print("Chu_vi =",p)
    print("Dien_tich =",s)
elif A== 'chữ_nhật':
    b = float(input("Nhập chiều rộng của hình chữ nhật: "))
    a = float(input("Nhập chiều dài của hình chữ nhật: "))
    p = 2 * (a + b)
    s = a * b
    print("Chu_vi =",p)
    print("Dien_tich =",s)
elif A== 'tròn':
    r = float(input("Nhập bán kính của hình tròn: "))
    p = 2 * math.pi * r
    s = math.pi * (r ** 2)
    print("Chu vi =",p)
    print("Dien_tich =",s)
else:
    print("Không tìm thấy hình. Vui lòng nhập lại ")

