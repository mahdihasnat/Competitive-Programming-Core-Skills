# -*- coding: utf-8 -*-

import sys

def main():
    n, W = map(int, input().split())
    items = [list(map(int, input().split())) for _ in range(n)]

    result = []

    dp = [[0] * (W +1)  for _ in range(n+1)]

    for i in range(1, n+1):
        w = items[i-1][0] 
        v = items[i-1][1] 

        for j in range( 1 ,W+1):
            dp[i][j] = dp[i-1][j]
            if j>= w :
                dp[i][j] = max(dp[i][j] , dp[i-1][j-w] + v)
        for j in range(1,W+1):
            dp[i][j] = max(dp[i][j] ,dp[i][j-1])

    # for i in range(n+1):
    #     print( " ".join(map(str , dp[i])))

    now = W
    cost = dp[n][W]

    for i in range(n , 0 , -1):
        
        # print(now ,end = ' ')
        # print(cost )
        w = items[i-1][0] 
        v = items[i-1][1] 
        
        if now >= w and dp[i-1][now - w] + v  == dp[i][now ] and cost > 0 :
            result.append(i)
            now -= w
            cost -= v

    assert(dp[0][now] == 0)
    result.reverse()

    print(len(result))
    print(" ".join(map(str, result)))


if __name__ == '__main__':
    main()
