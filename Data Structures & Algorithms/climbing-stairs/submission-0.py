class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # faut juste calculer Fn où Fn est la suite de fibonnacci
        # Fn = Fn-1 + Fn-2
        # F1 = 1, F2 = 2
        if n == 1:
            return 1
        F1, F2 = 1, 2
        for _ in range(2, n): # on commence à 2 comme ça climbStairs renvoie le bon output pour 1 et 2
            cur = F1 + F2
            F1, F2 = F2, cur
        return F2
        