#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__' :
    x1, y1, r1 = map(int, input().split(' '))
    x2, y2, r2 = map(int, input().split(' '))

    size_x_min = min([x1-r1, x2-r2])
    size_x_max = max([x1+r1, x2+r2])
    size_y_min = min([y1-r1, y2-r2])
    size_y_max = max([y1+r1, y2+r2])

    r1 = r1**2
    r2 = r2**2

    count = 0

    for y in range(size_y_min, size_y_max):
        for x in range(size_x_min, size_x_max):
            if (x1 - x)**2 + (y1 - y)**2 <= r1 and (x2 - x)**2 + (y2 - y)**2 <= r2:
                count += 1
    print(count)