class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l, best = 0, 0
        freq = defaultdict(int)
        for r in range(n):
            freq[s[r]] += 1
            maxFreq = max(freq.values())
            while (r-l+1) - maxFreq > k:
                freq[s[l]] -= 1
                l += 1
                maxFreq = max(freq.values())
            best = max(best, r-l+1)
        return best