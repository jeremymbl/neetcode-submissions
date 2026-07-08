class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if (n==0 or n%2 != 0):
            return False
        pile = []
        opening = {"(", "{", "["}
        dico = {")": "(","}": "{", "]": "["}
        
        for i in range(n):
            if s[i] in opening:
                pile.append(s[i])
            else:
                if len(pile) == 0:
                    return False
                if pile[-1] != dico[s[i]]:
                    return False
                else:
                    pile.pop()
        
        return len(pile) == 0
                    

