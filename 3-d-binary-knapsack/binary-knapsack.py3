# -*- coding: utf-8 -*-

import sys

def countTrailingZero(x): 
    count = 0
    while ((x & 1) == 0): 
        x = x >> 1
        count += 1
    return count 

def main():
    n , W = map(int ,  input() .split() )

    wv = [  list(map(int ,  input() .split() ) )  for _ in range(n) ]

    result = 0

    values = [ [] for i in range(35)]

    for z in wv:
        # print(z)
        values[countTrailingZero(z[0])].append(z[1])


    for i in range(34):
        
        values[i].sort()

        if (W>>i) & 1 !=0  and len(values[i]) > 0 :
            result += values[i][-1]
            values[i].pop()
        
        while len(values[i]) > 1 :
            values[i+1].append(values[i][-1] + values[i][-2])
            values[i].pop()
            values[i].pop()
        
        if len(values[i]) == 1 :
            values[i+1].append(values[i][-1])
        
    
    print( result )


if __name__ == '__main__':
    main()