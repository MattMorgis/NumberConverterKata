"""
Courtesy of James Grenning (@jwgrenning) and Jeff Langr (@jlangr).
Use this to learn TDD.

This module supplies one function, toWords():

>>> toWords(0)
'zero'

It uses doctest to test toWords with many examples like the one above.
It runs in Python 3 or Python 2.

Notes:
While the code below completes all the test cases it is crap and ripe for refactoring.
TODO:
1. Provide a number from 0->999 without looping.
2. Iterate over thousands instead of each power of 10.
3. Remove duplicate string functions and move all strings resources collection.
    - Use on resource for numbers 0-999.
    - Uses a second resource for thousands, millions, etc.
"""
import math

def toWords(n):
    """ Return a description, in words, of the integer passed to it.  

    >>> toWords(1)
    'one'

    >>> toWords(10)
    'ten'

    >>> toWords(19)
    'nineteen'

    >>> toWords(20)
    'twenty'

    >>> toWords(90)
    'ninety'

    >>> toWords(21)
    'twenty-one'

    >>> toWords(55)
    'fifty-five'

    >>> toWords(99)
    'ninety-nine'

    >>> toWords(100)
    'one hundred'

    >>> toWords(900)
    'nine hundred'

    >>> toWords(101)
    'one hundred one'

    >>> toWords(999)
    'nine hundred ninety-nine'

    >>> toWords(1000)
    'one thousand'

    >>> toWords(9000)
    'nine thousand'

    >>> toWords(9999)
    'nine thousand nine hundred ninety-nine'

    >>> toWords(9911)
    'nine thousand nine hundred eleven'

    >>> toWords(10000)
    'ten thousand'

    >>> toWords(19000)
    'nineteen thousand'
    
    >>> toWords(19999)
    'nineteen thousand nine hundred ninety-nine'
    
    >>> toWords(100000)
    'one hundred thousand'

    >>> toWords(700000)
    'seven hundred thousand'

    >>> toWords(198000)
    'one hundred ninety-eight thousand'

    >>> toWords(701020)
    'seven hundred one thousand twenty'

    >>> toWords(1000000)
    'one million'
    """

    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
  
    if n == 0:
        return "zero"

    words = ""
    dms = [] # division by 10 and modulo tuple results

    div = n
    while div > 0:
        dmtup = divmod(div, 10) 
        dms.append(dmtup)
        div = dmtup[0]
    
    pow10 = len(dms) - 1
    index = pow10
    dash = " "
    hasThousands = False
    while(index >= 0):
        div = dms[index][0]
        mod = dms[index][1]
        if index == 0:
            if mod != 0 and words != "":
                words = words + dash
            words = words + _toOnes(mod)
        elif index == 1:
            if mod == 1 and dms[index-1][1] != 0:
                if words != "":
                    words = words + dash                
                words = words + _toTeens(dms[index-1][1])
                index = index - 1
            else:
                tens = _toTens(mod)
                if mod != 0 and words != "":
                    words = words + dash
                words = words + tens                
                if tens != "":
                    dash = "-"
        elif index == 2:
            if mod != 0 and words != "":
                words = words + dash
            words = words + _toHundreds(mod)
        elif index == 3:
            if mod != 0 and words != "":
                words = words + dash
            hasThousands = hasThousands or (mod != 0)                
            words = words + _toOnes(mod)
            if hasThousands:
                words = words + " thousand"
            tens = ""
        elif index == 4:
            if mod == 1 and dms[index-1][1] != 0:
                if words != "":
                    words = words + dash                
                words = words + _toTeens(dms[index-1][1]) + " thousand"
                index = index - 1
            else:
                tens = _toTens(mod)
                if mod != 0 and words != "":
                    words = words + dash
                words = words + tens                
                if tens != "":
                    dash = "-"
            hasThousands = hasThousands or (mod != 0)    
        elif index == 5:
            if mod != 0 and words != "":
                words = words + dash            
            words = words + _toHundreds(mod)
            hasThousands = hasThousands or (mod != 0)
        elif index == 6:
            if mod != 0 and words != "":
                words = words + dash            
            words = words + _toMillions(mod)
        index = index - 1

    return words

def _toOnes(i):
    if not (i >= 0 and i <= 9):
        raise ValueError("i must be >= 0 and <=9")
    ones = ("", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    return ones[i]

def _toTeens(i):
    if not (i >= 0 and i <= 9):
        raise ValueError("i must be >= 0 and <=9")
    if i == 0:
        return ""
    if i == 1:
        return "eleven"
    elif i == 2:
        return "twelve"
    elif i == 3:
        return "thirteen"
    elif i == 5:
        return "fifteen"
    else:
        return _toOnes(i)+"teen"

def _toTens(i):
    if not (i >= 0 and i <= 9):
        raise ValueError("i must be >= 0 and <=9")
    tens = ("", "ten", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety")
    return tens[i]

def _toHundreds(i):
    if i == 0:
        return ""
    else:
        return _toOnes(i) + " hundred"

def _toThousands(i):
    if i == 0:
        return ""
    else:
        return _toOnes(i) + " thousand"

def _toTeenThousands(i):
    if i == 0:
        return ""
    else:
        return _toTeens(i) + " thousand"


def _toTenThousands(i):
    if i == 0:
        return ""
    else:
        return _toTens(i) + " thousand"

def _toHundredThousands(i):
    if i == 0:
        return ""
    else:
        return _toHundreds(i) + " thousand"

def _toMillions(i):
    if i == 0:
        return ""
    else:
        return _toOnes(i) + " million"

# run doctest on above tests if this file is directly as main
if __name__ == "__main__":
    import doctest
    doctest.testmod()