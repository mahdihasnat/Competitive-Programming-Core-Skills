# -*- coding: utf-8 -*-

import sys

def calc(xy, mask):
    ret = 0
    if mask&2 == 0 :
        ret += xy[0]
    else :
        ret -= xy[0]

    if mask&1 == 0 :
        ret += xy[1]
    else :
        ret -= xy[1]
    return ret
def distance(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def main():
    n = int(input())
    points = [ list(map(int , input().split()) ) for _ in range(n)]

    candidate  = [ 0 for _ in range(4) ]

    for i in range(n):
        
        for j in range(4):
            if calc(points[ candidate[j] ] , j ) < calc(points[i]  , j ):
                candidate[j] = i
        
        # print( candidate )

        lo = candidate[0]
        hi = candidate[1]

        for x in range(4) :
            for y in range(x+1, 4) :
                if distance( points[ candidate[x] ]  , points[ candidate[y] ] ) > distance( points[ lo ] , points[ hi ]):
                    lo = candidate[ x ]
                    hi = candidate[ y ]

        print( "{} {}".format(lo+1 , hi+1) )


if __name__ == '__main__':
    main()