# -*- coding: utf-8 -*-

import sys

def main():
    n = int(input())
    points = [ int(input()) for _ in range(n)]

    lo = 0 
    hi = 0

    for i in range(n):
        if points[i] < points[lo] :
            lo = i

        if points[i] > points[hi] :
            hi = i

        print( "{} {}".format(lo+1 , hi+1) )


if __name__ == '__main__':
    main()