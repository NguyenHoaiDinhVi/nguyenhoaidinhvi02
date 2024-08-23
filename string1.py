# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 01:07:25 2024

@author: nguyenhoaidinhvi
"""

print("bài 1")
a= " Đại học Quốc gia, Khu phố 6, P.Linh Trung, Q.Thủ Đức, Tp.HCM"
print(" Đại học Quốc gia\n Khu phố 6\n P. Linh Trung\n Q. Thủ Đức\n Tp.HCM")
print("bài 2")
print(a.replace("P.","").replace("Q.","").replace("Tp.","").replace(",","\n"))