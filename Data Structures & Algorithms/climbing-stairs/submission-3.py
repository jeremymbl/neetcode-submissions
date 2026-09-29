class Solution:
    def climbStairs(self, n: int) -> int:
        # on fait recursivement mais terminale 
        def aux(a, b, n):
            if n == 1:
                return 1
            if n == 2:
                return b
            else:
                return aux(b, a+b, n-1)
        return aux(1, 2, n)