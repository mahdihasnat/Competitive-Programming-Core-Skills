# -*- coding: utf-8 -*-

import sys
import math

def main():
    x, y = map(int, input().split())
    result = 0

    if y< 0 :
        x= -x
        y =-y

    result = (x+y-1)//y

    print(result)


if __name__ == '__main__':
    main()