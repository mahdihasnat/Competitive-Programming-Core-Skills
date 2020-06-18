# -*- coding: utf-8 -*-

import sys



def main():
    n = int(input())
    a =[0]+  list(map(int , input().split()))
    
    # for i in range(1,n+1):
    #     print( a[i] ) 

    ans = [ 0 for _ in range(n+2)]
    
    qsum = 0 
    qmin = 0

    for i in range(1,n+1):
        ans [i] += qsum - qmin
        qsum += a[i]
        qmin = min( qsum , qmin )
    
    qsum = 0 
    qmin = 0

    for i in range(n,0, -1):
        ans [i] += qsum - qmin
        qsum += a[i]
        qmin = min( qsum , qmin )
    
    for i in range(1,n+1):
        ans[i] += a[i]
    
    print( " " .join( map( str , ans[1:n+1]) ) )


if __name__ == '__main__':
    main()