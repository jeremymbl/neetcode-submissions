class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False
        pile = []
        opening_set = set(("(", "{", "["))
        hash_opposite = {")": "(", "}": "{", "]": "["}
    
        for i in range(n):
            if s[i] in opening_set:
                pile.append(s[i])
            else:
                if not pile or pile[-1] != hash_opposite[s[i]]:
                    return False
                else:
                    pile.pop()
        return len(pile)==0
