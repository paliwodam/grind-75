# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
# The algorithm for myAtoi(string s) is as follows:
# Whitespace: Ignore any leading whitespace (" ").
# Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
# Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
# Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
# Return the integer as the final result.

class Solution:
    def myAtoi(self, s: str) -> int:
        n, i = len(s), 0
        while i < n and s[i].isspace():
            i += 1
        if i == n: return 0

        sign = 1
        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "+": 
            i += 1
        
        while i < n and s[i]  == "0":
            i += 1

        result = 0
        while i < n:
            if not s[i].isdigit():
                return result * sign
            if result > 2 ** 31 // 10:
                return -2 ** 31 if sign == -1 else 2 ** 31 - 1
            next_digit = int(s[i])
            if result == 2**31 // 10:
                if sign == -1:
                    next_digit = min(next_digit, 2**31 % 10)
                else:
                    next_digit = min(next_digit, (2**31 - 1) % 10)
            result *= 10 
            result += next_digit
            i += 1
    
        return result * sign

