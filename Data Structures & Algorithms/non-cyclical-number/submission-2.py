class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            digits = [int(d)**2 for d in str(n)]
            n = sum(digits)
            if n in seen:
                return False
            else:
                seen.add(n)
        return True


        