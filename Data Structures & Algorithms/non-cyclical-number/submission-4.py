class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {n}
        while n != 1:
            n = sum([int(d)**2 for d in str(n)])
            if n in seen:
                return False
            else:
                seen.add(n)
        return True