# -*- coding: utf-8 -*-

import sys

def main():
    n = int(input())
    points = [ list(map(int , input().split()) ) for _ in range(n)]
    
    qsum  = [ 0 for _ in range(100005)]

    for lr in points:
        qsum[lr[0]] += 1 
        qsum[lr[1]+1] -= 1 
    
    for i in range(1 , 100005):
        qsum[i] += qsum[i-1]
        if qsum[i] > 0 :
            print("{} {}".format(i , qsum[i] ))



if __name__ == '__main__':
    main()