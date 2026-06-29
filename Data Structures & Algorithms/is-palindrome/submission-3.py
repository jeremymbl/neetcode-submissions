class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = "".join(c for c in s.lower() if c.isalnum())
        res = True
        n = len(r)
        for i in range(n//2):
            res = res and (r[i] == r[len(r)-1-i])
        return res