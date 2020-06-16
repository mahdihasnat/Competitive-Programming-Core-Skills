# -*- coding: utf-8 -*-

import sys


def main():
    n = int(input())
    a = list( map( int , input().split() ))

    result = 0

    minimums  = [10000000  for _ in range(n) ]

    for i in range(n):
        for j in range(i+1):
            minimums[j] =  min( minimums[j] , a[i] ) 
            result += minimums[j]

    print(result)


if __name__ == '__main__':
    main()