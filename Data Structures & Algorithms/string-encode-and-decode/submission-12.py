class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += "#" + f"{len(word)}" + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        n = len(s)
        res = []
        i = 0
        while i < n:
            j = i+1
            length = ""
            while s[j] != "#":
                length += s[j]
                j += 1
            length = int(length)
            res.append(s[j+1: j+1+length])
            i = j+1+length
        return res
