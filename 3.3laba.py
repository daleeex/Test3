#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

if __name__ == '__main__':
    n=int(input("Value of n?"))
    x=float(input("Value of x?"))
    S = 0.0
    for k in range (1, n+1):
        a = math.log(k*x) / (k*k)
        S+=a
        
    print(f"S= {S}")