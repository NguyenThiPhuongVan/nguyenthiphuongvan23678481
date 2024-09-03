#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 12:33:54 2024

@author: nguyenthiphuongvan2005
"""

import math
r = float(input("Nhập bán kính của hình tròn: "))
        
cv = 2*math.pi*r
s = cv**2/4*math.pi

print ("Chu vi: ", cv)
print ("Diện tích: ", s)


