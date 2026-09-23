class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for word in strs:
            occ_list = [0]*26
            for letter in word:
                i = ord("a") - ord(letter)
                occ_list[i] += 1
            occ_tuple = tuple(occ_list)
            if occ_tuple in d:
                d[occ_tuple].append(word)
            else:
                d[occ_tuple] = []
                d[occ_tuple].append(word)
        return list(d.values())
