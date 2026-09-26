class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        boo = False
        while n != 1 and not(boo):
            digits = [int(d) for d in str(n)]
            n = sum([x**2 for x in digits])
            if n in seen:
                boo = True
            else:
                seen.add(n)
        return not(boo)


        