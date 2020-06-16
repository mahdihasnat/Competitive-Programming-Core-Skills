# -*- coding: utf-8 -*-

import sys

def next_permutation(a):
    """Generate the lexicographically next permutation inplace.

    https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
    Return false if there is no next permutation.
    """
    # Find the largest index i such that a[i] < a[i + 1]. If no such
    # index exists, the permutation is the last permutation
    for i in reversed(range(len(a) - 1)):
        if a[i] < a[i + 1]:
            break  # found
    else:  # no break: not found
        return False  # no next permutation

    # Find the largest index j greater than i such that a[i] < a[j]
    j = next(j for j in reversed(range(i + 1, len(a))) if a[i] < a[j])

    # Swap the value of a[i] with that of a[j]
    a[i], a[j] = a[j], a[i]

    # Reverse sequence from a[i + 1] up to and including the final element a[n]
    a[i + 1:] = reversed(a[i + 1:])
    return True
def calc_cost( n , a,perm):
    ret  = 0
    for i in range(n-1):
        ret += a[perm[i]][perm[i+1]]
    return ret

def main():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]

    result = []
    perm =  [ i for i in range(n)]
    ans = 10000000

    while 1 :
#        print( perm )
        now = calc_cost(n,a,perm)
        if now < ans :
            ans = now 
            result = perm[ : ]
        if not next_permutation(perm) :
            break
    
    for i in range(n):
        result[i] +=1
    


    print(" ".join(map(str,result)))


if __name__ == '__main__':
    main()