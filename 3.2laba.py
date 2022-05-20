#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    n= int (input("Введите номер месяца"))

    if n == 1 or n ==2 or n ==12 :
        print("Winter")
    elif n == 3 or n ==4 or n==5 :
        print("Spring")
    elif n==6 or n==7 or n==8 :
        print("Summer")
    elif n==9 or n==10 or n == 11 :
        print("Autumn")
    else:
        print("Error!", file =sys.stderr)
        exit(1)