class Solution:

    def characterReplacement(self, s: str, k: int) -> int:

        l = 0

        best = 0

        seen = defaultdict(int)

        for r in range(len(s)):

            seen[s[r]] += 1

            maxFreq = max(seen.values())

            while (r - l + 1) - maxFreq > k:

                seen[s[l]] -= 1

                l += 1

                maxFreq = max(seen.values())

            best = max(best, r - l + 1)

        return best
        