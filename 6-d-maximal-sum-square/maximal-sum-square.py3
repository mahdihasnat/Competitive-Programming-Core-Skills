# -*- coding: utf-8 -*-

import sys

def sum(qsum , i, j, k):
    return qsum[i][j] - qsum[i-k][j] - qsum[i][j-k] + qsum[i-k][j-k]

def main():
    n , k = map ( int , input().split() )

    a = [ list( map(int , input().split())) for _ in range(n) ]

    qsum = [ [0] * (n+1) for _ in range(n+1)]
    
    result = 0

    # for i in range(n):
    #     print(" ".join(map(str , a[i])))

    for i in range(1,n+1):
        for j in range(1,n+1):
            qsum[i][j] += qsum[i][j-1] +a[i-1][j-1]
        for j in range(1,n+1):
            qsum[i][j] +=qsum[i-1][j]
    for i in range(k,n+1):
        for j in range(k,n+1):
            result = max(result , sum(qsum ,i,j,k))

    print(result)

if __name__ == '__main__':
    main()
