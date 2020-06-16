# -*- coding: utf-8 -*-

import sys

def main():
    x, y, z = map(int, input().split())
    result = -1

    # your code3

    now = 0

    if now == z :
        result  = 0 
    else : 
        
        for i in range(1,20005):
            
            if i % 2 == 1 :
                now = now + x
            else :
                now = now - y
            if now == z :
                result = i
                break
            

    print(result)


if __name__ == '__main__':
    main()