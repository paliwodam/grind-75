# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

# The algorithm for myAtoi(string s) is as follows:

# Whitespace: Ignore any leading whitespace (" ").
# Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
# Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
# Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
# Return the integer as the final result.

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if len(s) == 0: return 0
        sign = 1
        if s[0] in ["-", "+"]:
            if s[0] == "-": sign = -1
            s = s[1:]

        s = s.lstrip("0")
        result = 0
        for c in s:
            if not c.isdigit():
                break
            
            result *= 10
            result += int(c)
        result *= sign
        result = min(result, 2**31 -1)
        result = max(result, -2**31)
        return result 

