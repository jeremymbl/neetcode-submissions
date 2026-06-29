class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = "".join(c for c in s.lower() if c.isalnum())
        n = len(r)

        for i in range(n // 2):
            if r[i] != r[n - 1 - i]:
                return False

        return True