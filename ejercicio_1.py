# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 14:58:41 2020

@author: luisr
"""

import math
Unidad=["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
Decena=["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
Centena=["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
Millar=["","M","MM","MMM",]
N=int(input("Ingresa numero entero\n"))
u= N % 10
d=int(math.floor(N/10))%10
c=int(math.floor(N/100))%10
m=int(math.floor(N/1000))
print(Millar[m]+Centena[c]+Decena[d]+Unidad[u])