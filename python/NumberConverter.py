"""
Courtesy of James Grenning (@jwgrenning) and Jeff Langr (@jlangr).
Use this to learn TDD.

This module supplies one function, toWords():

>>> toWords(0)
'zero'

It uses doctest to test toWords with many examples like the one above.
It runs in Python 3 or Python 2.

Notes:
This implementation works into trillions.
It can be expanded beyond trillions by:
- modifiying the range check on the argument at the beginning of toWords()
- adding additional descriptive words to _illions resource at the end of this file.
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

    >>> toWords(999019933747026)
    'nine hundred ninety-nine trillion nineteen billion nine hundred thirty-three million seven hundred forty-seven thousand twenty-six'
    
    """

    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n >= 1e15:
        raise ValueError("n too large")
  
    if n == 0:
        return "zero"
    words = ""

    dms = [] # division and modulo tuple result list
    # power of 1000 is index into list
    # each modulo result will contain 0-999 for that power of 1000 
    # div part is what is left to keep dividing
    div = n
    while div > 0:
        dmtup = divmod(div, 1000) 
        dms.append(dmtup)
        div = dmtup[0]
    
    # loop build the string based on modulo 1000 tuple list results
    pow1000 = len(dms) - 1
    while pow1000 >= 0:
        (div, mod) = dms[pow1000]
        modwords = _to999(mod) 
        cat = _space if words and modwords else ''
        words = words + cat + modwords 
        if pow1000 > 0 and modwords:
                words = words + _space + _illions[pow1000]
        pow1000 = pow1000 - 1

    return words


def _to999(i):
    wr = ""
    if i>=100:
        (d, m) = divmod(i, 100)
        wr = _ones[d] + _space + _hundred
        if m == 0:
            return wr
        wr = wr + _space
        i = m
    if i>=10:
        (d, m) = divmod(i, 10)
        if m == 0:
            return wr + _tens[d]
        if d == 1:
            return wr + _teens[m]
        wr = wr + _tens[d] + _dash
        i = m
    wr = wr + _ones[i]
    return wr

# string resources
_zero = "zero"
_space = " "
_dash = "-"
_ones = ("", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
_tens = ("", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety")
_teens = ("", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen")
_hundred = "hundred"
_illions = ("", "thousand", "million", "billion", "trillion")

# run doctest on above tests if this file is directly as main
if __name__ == "__main__":
    import doctest
    doctest.testmod()