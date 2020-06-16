# -*- coding: utf-8 -*-

import sys

def number (ch):
    if ord('2') <= ord(ch) <= ord('9'):
        return ord(ch) - ord('0')
    if ch == 'T':
        return 10
    if ch == 'J':
        return 11
    if ch == 'Q':
        return 12
    if ch == 'K':
        return 13
    if(ch == 'A'):
        return -1
    
    

def main():
    
    s = list( map ( str , input().split() ))
    
    result = "NO"
    suits =set()

    for i in range(5):
        suits.add(s[i][1])
    
    if len(suits) == 1 :
        
        num = []

        for i in range(5):
            num.append(number(s[i][0]))
        num.sort()

        if num[0]== -1 :
            if num[-1] - num[1] == 3 and (num[1] == 2 or num[-1] == 13):
                result  = "YES"
        elif num[-1] - num[0] == 4:
            result  = "YES"


    print(result)


if __name__ == '__main__':
    main()