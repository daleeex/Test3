#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys

# Точность вычислений.
EPS = 1e-10

if __name__ == '__main__' :
    x = float ( input (" x = ") )
    if x == 0:
        print ( "Ошибка" , file=sys.stderr )
        exit (1)

    a = -(3*x) ** 1/3
    S, n = a, 1
    # Найти сумму членов ряда.
    while math.fabs(a) > EPS:
        a *= (-1) * ((2 * n + 1) * x ** 2) / ((2 * n + 3) * (n + 1))
        S += a
        n += 1
    # Вывести значений функций. 
    print( f"erf({x}) = {2 / math.sqrt(math.pi) + S}" )