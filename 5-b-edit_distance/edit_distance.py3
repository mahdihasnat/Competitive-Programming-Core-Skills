# -*- coding: utf-8 -*-

import sys

def main():
    n, m = map(int, input().split())
    u ="z"  + input().strip()
    w = "a" + input().strip()
    I, D, S = map(int, input().split())

    result = 0
    
    dp = [ [ 10000000] * (m+1) for _ in range(n+1)  ] 

    dp[0][0] = 0

    for i in range(0,n+1):
        for j in range(0,m+1):
            if  i> 0  and j> 0 and u[i] == w[j]:
                dp[i][j] = dp[i-1][j-1]
            if i>0 :
                dp[i][j] = min(dp[i][j] , dp[i-1][j] + D)
            if j>0 :
                dp[i][j] = min(dp[i][j] , dp[i][j-1] + I)
            if i>0 and j> 0 :
                dp[i][j] = min(dp[i][j] , dp[i-1][j-1] + S)

    # for i in range(n+1):
    #     print( " ".join(map(str ,dp[i]) ) )


    result = dp[n][m]

    print(result)


if __name__ == '__main__':
    main()