# -*- coding: utf-8 -*-

import sys

def main():
    x = str(input())
    n = len(x)

    result = n
    if x == "9" * n :
        result = result + 1


    print(result)


if __name__ == '__main__':
    main()