import math
class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(5,n+1):
            for j in range(3,i):
                c = i**2 - j**2
                if math.isqrt(c)**2 == c: res += 1
        return res