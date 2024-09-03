#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:59:18 2024

@author: nguyenthiphuongvan2005
"""


bien_so_xe=input("Nhập biển số xe: ")

tong=sum(int(chu_so) for (chu_so) in (bien_so_xe))

hang_chuc=tong//10

hang_don_vi=tong%10

sonut=hang_chuc+hang_don_vi

print(f"Vậy xe có {sonut} nút")
