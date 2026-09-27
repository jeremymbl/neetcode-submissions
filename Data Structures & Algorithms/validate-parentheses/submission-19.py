class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        pile = []
        open_brackets = {'(', '{', '['}
        close_brackets = {')', '}', ']'}
        bracket_map = {
                ')': '(',
                '}': '{',
                ']': '['
                }
        if n%2 == 1:
            return False
        for i in range(n):
            if s[i] in open_brackets:
                pile.append(s[i])
            else:
                if pile != [] and pile[-1] == bracket_map[s[i]]:
                    pile.pop()
                else:
                    return False
        return len(pile) == 0