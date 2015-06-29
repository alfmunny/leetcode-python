__author__ = 'alfmunny'

'''
Title:

Roman to Integer

Questions:

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''


class Solution:
    # @param {string} s
    # @return {integer}

    def __init__(self):
        pass

    def romanToInt(self, s):
        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        res = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]

        return res + roman[s[-1]]

def main():
    roman_s = "MDCLLXII"
    s = Solution()
    print s.romanToInt(roman_s)

if __name__ == '__main__':
    main()
