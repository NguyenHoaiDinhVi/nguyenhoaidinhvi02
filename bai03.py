# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 01:15:16 2024

@author: nguyenhoaidinhvi
"""
print("nhập 1 số nguyên dương có 2 chữ số")
a=int(input("a="))
if a<=99 and a>=1:
    x=a%10
    y=a//10
    b=x+y
    print("tổng các chữ số=",b)
else:
    print("không xác định")   
