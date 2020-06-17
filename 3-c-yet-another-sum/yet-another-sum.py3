# -*- coding: utf-8 -*-

import sys
from fractions import Fraction

def main():
    n = int( input())
    x = list( map(int , input().split()))

    #getcontext().prec = 15

    result = Fraction(0)

    for xi in x:
        result += Fraction(xi) + Fraction(1) / Fraction(xi)
    
    print( "{:.15f}".format( result.numerator/result.denominator ) )


if __name__ == '__main__':
    main()