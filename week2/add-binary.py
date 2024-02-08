# Given two binary strings a and b, return their sum as a binary string.

 

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n_a, n_b = len(a), len(b)
        i, j = n_a - 1, n_b - 1
        k = max(n_a, n_b) 
        res = [""] * (k+1)
        carry = 0
        
        while i >= 0 or j >= 0 or carry:
            if i >= 0 and j >= 0:
                added = int(a[i]) + int(b[j]) + carry
                i -= 1
                j -= 1
            elif i >= 0:
                added = int(a[i]) + carry
                i -= 1
            elif j >= 0:
                added = int(b[j]) + carry
                j -= 1
            else: 
                added = carry
            
            res[k] = str(added % 2)
            carry = added // 2
            k -= 1
        
        res_string =("").join(res)
        if len(res_string) > 1 and res_string[0] == "0":
            return res_string[1:]
        return res_string


