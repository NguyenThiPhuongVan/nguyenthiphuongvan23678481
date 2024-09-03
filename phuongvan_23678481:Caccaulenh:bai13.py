#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 14:23:13 2024

@author: nguyenthiphuongvan2005
"""

A = int(input("Nhập ngày sinh: "))
B = int(input("Nhập tháng sinh: "))
C = int(input("Nhập năm sinh: "))


dinh_dang_a = (f"{A}/{B}/{C}")
print(f"a) {dinh_dang_a}")


dinh_dang_b = (f"{A}/{B}/{str(C)[-2:]}")
print(f"b) {dinh_dang_b}")


dinh_dang_c = (f"{C}/{B}/{A}")
print(f"c) {dinh_dang_c}")
