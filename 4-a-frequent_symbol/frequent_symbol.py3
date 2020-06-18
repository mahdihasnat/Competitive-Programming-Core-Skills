# -*- coding: utf-8 -*-

import sys

def main():
    s = input()
    q = int(input())
    a = [list(map(int, input().split())) for _ in range(q)]

    n = len(s)

    frequency = [[0  for _ in range(26) ] for _ in range(n+1)]

    for i in range(1,n+1):
        frequency[i] = frequency[i-1][:]
        frequency[i][ int(ord(s[i-1]) - ord('a'))] +=1
        # print( " ".join( map( str , frequency[i] ) ) )



    result = []

    for lr  in a :
        l = lr[0] 
        r = lr[1]
        cnt = [ frequency[r][i] - frequency[l-1][i] for i in range(26) ]
        mx = 0 
        for i in range(26):
            if cnt[i] > cnt[mx] :
                mx = i
        result.append( chr(ord('a') +mx) )

    
    print("\n".join(result))


if __name__ == '__main__':
    main()