'''
Implement pow(x, n), which calculates x raised to the power n (xn).
Example 1:
Input: 2.00000, 10
Output: 1024.00000
Example 2:
Input: 2.10000, 3
Output: 9.26100
Example 3:
Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:
-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
'''


class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        neg_pow = n < 0
        if neg_pow:
            x = 1 / x
            n *= -1

        final_val = 1
        powe = x
        while n:
            if n & 1:
                final_val *= powe
            powe *= powe
            n = n >> 1
        return final_val