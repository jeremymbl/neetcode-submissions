class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l, best = 0, 0 
        countChar = defaultdict(int)
        for r in range(n):
            countChar[s[r]] += 1
            maxFreq = max(countChar.values())
            while r-l+1-maxFreq > k:
                countChar[s[l]] -= 1
                l += 1
                maxFreq = max(countChar.values())
            best = max(best, r-l+1)
        return best