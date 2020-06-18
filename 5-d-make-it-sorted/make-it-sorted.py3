# -*- coding: utf-8 -*-

import sys

def main():
    n = int( input() )
    a = list( map ( lambda x : int(x)+2000  ,input().split() ) )
    result = 0

    dp = [ [10000000] * ( 50000 )  for _ in range(2) ] 
    now = 0

    for i in range(n):
        now = now ^ 1
        prev = 10000000
        for j in range(5000):
            dp[now][j] = abs(j - a[i])
            if i> 0 :
                prev = min( prev , dp[now ^ 1][j])
                dp[now][j] += prev

    result = min(dp[now])

    print(result)


if __name__ == '__main__':
    main()