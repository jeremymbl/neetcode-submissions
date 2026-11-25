class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        counter_s, counter_t = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            counter_s[s[i]] += 1
        for j in range(len(t)):
            counter_t[t[j]] += 1
        return counter_s == counter_t