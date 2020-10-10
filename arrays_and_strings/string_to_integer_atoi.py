# Implement atoi which converts a string to an integer.

# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

# If no valid conversion could be performed, a zero value is returned.

# Note:

# Only the space character ' ' is considered a whitespace character.
# Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
 

# Example 1:

# Input: str = "42"
# Output: 42
# Example 2:

# Input: str = "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus sign. Then take as many numerical digits as possible, which gets 42.
# Example 3:

# Input: str = "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
# Example 4:

# Input: str = "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a numerical digit or a +/- sign. Therefore no valid conversion could be performed.
# Example 5:

# Input: str = "-91283472332"
# Output: -2147483648
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer. Thefore INT_MIN (−231) is returned.
 

# Constraints:

# 0 <= s.length <= 200
# s consists of English letters (lower-case and upper-case), digits, ' ', '+', '-' and '.'.

class Solution:
    #Works but should do w/o int and manually compute (under)overflow conditions
    def myAtoi(self, s: str) -> int:
        ans = 0
        s = s.lstrip()
        if len(s) == 0 or s[0] not in '+-0123456789':
            return 0
        else:
            int_min = -2147483648
            int_max = 2147483647
            for i, char in enumerate(s):
                if char in '+-' and i < (len(s)-1) and s[i+1] in '0123456789':
                    if char == '-':
                        neg = True
                    else:
                        neg = False
                    start = i+1
                    break
                elif (char in '0123456789'):
                    neg = False
                    start = i
                    break
                else: 
                    return 0
            stop = start+1
            for i, char in enumerate(s[(start+1):]):
                if char not in '0123456789':
                    stop = i + start + 1
                    break
                elif (i+start+1) == (len(s)-1):
                    stop = i+start+2
                    break
            ans = int(s[start:stop])
            if neg:
                ans = -ans
            if ans < int_min:
                ans = int_min
            elif ans > int_max:
                ans = int_max
        return ans