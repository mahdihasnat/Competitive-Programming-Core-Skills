# -*- coding: utf-8 -*-

import sys

def parse(text):
    chunks = ['']

    for character in text:
        if character.isdigit():
            if chunks[-1].isdigit():   # If the last chunk is already a number
                chunks[-1] += character  # Add onto that number
            else:
                chunks.append(character) # Start a new number chunk
        elif character in '+-/*':
            chunks.append(character)  # This doesn't account for `1 ++ 2`.

    return chunks[1:]

def main():
    a =  parse (input().strip())
    
    result = 0

    sign = 1

    for i in a :
        if i[0] == '+':
            sign = 1
        elif i[0] == '-':
            sign = -1
        else :
            result += sign * int(i)

    print(result)


if __name__ == '__main__':
    main()



### official solution
##python2
#def sub(s):
#    a = map(int, s.split('-'))
#    return a[0] * 2 - sum(a)

#def main():
#    s = raw_input()
#    add = s.split('+')
#    print sum(map(sub, add))
    
    
#if __name__ == '__main__':
#    main()