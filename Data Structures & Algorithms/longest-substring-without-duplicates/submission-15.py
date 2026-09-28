class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, best = 0, 0 
        n = len(s)
        seen = set()
        for r in range(n):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            best = max(best, r-l+1)
        return best