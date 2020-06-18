# -*- coding: utf-8 -*-

import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))

    result = 0
    lis  = [1] * n
    for i in range(n):
        for j in range(i):
            if a[j] < a[i]:
                lis[i] = max(lis[j] +1 , lis[i])
        
    result = max(lis)

    # your code

    print(result)


if __name__ == '__main__':
    main()
