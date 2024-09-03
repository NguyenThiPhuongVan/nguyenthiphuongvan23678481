#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:30:26 2024

@author: nguyenthiphuongvan2005
"""

N = int(input("Nhập số nguyên N: "))
if N > 0 :
    N = str(N)
N = "".join(sorted(N))
N = int(N)
print("Số có các chữ số theo thứ tự tăng  :", N)
if N < 0 :
    print("Số nhập vào phải là số nguyên ")