class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        best = 0
        seen = set()    
        n = len(s)
        for r in range(n):
            if s[r] not in seen:
                best = max(best, r-l+1)
                seen.add(s[r])
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                    best = max(best, r-l+1)
                seen.add(s[r])
        return best


        
            
