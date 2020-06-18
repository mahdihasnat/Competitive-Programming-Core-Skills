# -*- coding: utf-8 -*-

import sys

def main():
    n = int(input())
    m = list(map(int, input().split()))

    result = 0

    ans =[ [1000000000000000000] * n for _ in range(n) ]

    for i in range(n):
        for j in range(i+1):
            ans[i][j] = 0

    for len in range(1 , n+1):
        for l in range( n):
            r = l + len - 1
            if r >= n :
                break 
            
            for j in range(l ,r ):
                ans[l][r] = min(ans[l][r] ,  ans[l][j] + ans[j+1][r] + m[l] * m[j+1] * m[r+1])

    # for i in range(n):
    #     print( " ".join(map(str , ans[i] )))

    result = ans[0][n-1]

    print(result)


if __name__ == '__main__':
    main()
