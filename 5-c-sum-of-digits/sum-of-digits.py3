# -*- coding: utf-8 -*-

import sys

def main():
    s, l = map(int, input().split())
    
    result = 0

    dp = [ [0] * (s+1) for _ in range(l+1) ]

    dp[0][0] = 1

    for length in range (1 , l+1):
        for sum in range(0 , s+1):
            for digit in range(10):
                if digit <= sum:
                    dp[length][sum] += dp[length-1][sum - digit]
    if l>1 :
        result = dp[l][s] - dp[l-1][s]
    elif  s > 9 :
        result = 0
    else        :
        result = 1
    

    print(result)


if __name__ == '__main__':
    main()