# -*- coding: utf-8 -*-

import sys


def main():
    r, c = map(int, input().split())
    result = 0

    result += r * c - ( (r+2)//3 )*( (c+2)//3 )

    print(result)


if __name__ == '__main__':
    main()