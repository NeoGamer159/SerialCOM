# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 13:19:37 2022

@author: cernym
"""

my_str = "sample code for conversion"
my_str_encoded = my_str.encode(encoding = 'UTF-8')
print(my_str_encoded)
for bytes in my_str_encoded:
    print(bytes,end ='')