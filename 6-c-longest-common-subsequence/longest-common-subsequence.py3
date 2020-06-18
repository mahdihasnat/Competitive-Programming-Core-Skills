# -*- coding: utf-8 -*-

import sys

def main():
    n = int(input())
    a = [0] + list(map(int, input().split()))
    b = [0] + list(map(int, input().split()))

    result = 0

    dp = [ [0] * (n+1) for _ in range(n+1) ]

    for i in range(1,n+1):
        for j in range(1,n+1):
            if a[i] == b[j]:
                dp[i][j]  = dp[i-1][j-1] + 1
            else :
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
    result  = dp[n][n]
    x = []
    y = []

    i = n
    j = n

    while i> 0 and j> 0 :
        if a[i] == b[j] :
            x.append(i-1)
            y.append(j-1)
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i-1][j]:
            i -= 1
        else :
            j -= 1
    x.reverse()
    y.reverse()

    print(result)
    print(" ".join(map(str , x)))
    print(" ".join(map(str , y)))

if __name__ == '__main__':
    main()
