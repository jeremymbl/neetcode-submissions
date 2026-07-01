class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            res += "#" + str(len(word)) + "#" + word

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # Find the second #, which marks the end of the length
            j = i + 1

            while s[j] != "#":
                j += 1

            length = int(s[i + 1:j])

            # The word starts right after the second #
            word_start = j + 1
            word_end = word_start + length

            res.append(s[word_start:word_end])

            # Move i to the beginning of the next encoded word
            i = word_end

        return res