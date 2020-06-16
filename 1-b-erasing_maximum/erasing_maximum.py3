# -*- coding: utf-8 -*-

import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))

    result = []

    # your code

    max  = a[0]
    for i in range (1,n):
        if max < a[i] :
            max = a[i]

    occurence  = []
    for i in range(n):
        if a[i] == max :
            occurence.append(i)
    for i in range(n):
        if a[i] == max and (len(occurence) == 1  or occurence[2] == i):
            pass
        else :
            result.append(a[i])
    



    print(" ".join(map(str,result)))


if __name__ == '__main__':
    main()