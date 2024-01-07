'''
https://leetcode.com/problems/reverse-integer/description/

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

'''

class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = x * sign
        y = 0
        while x != 0:
            y += x % 10            
            if x // 10 == 0:                
                break                
            else:
                x //=  10
                y *= 10            
        if y > 2**31 - 1 or y < -2**31:
            return 0
        return y * sign
    
sol = Solution()
print(sol.reverse(123))