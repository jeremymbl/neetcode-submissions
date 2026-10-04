class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 0 
        l = 0
        n = len(s)
        maxFreq = 0 
        freqCount = defaultdict(int)
        for r in range(n):
            freqCount[s[r]] += 1
            maxFreq = max(freqCount.values())
            while (r-l+1) - maxFreq > k:
                freqCount[s[l]] -= 1
                l += 1
            best = max(best, r-l+1)
        return best

