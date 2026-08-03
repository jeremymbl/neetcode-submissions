class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        d = defaultdict(list)
        for word in strs:
            occ_list = [0]*26
            for s in word:
                occ_list[ord(s)-ord("a")] += 1
            occ_tuple = tuple(occ_list)
            d[occ_tuple].append(word)
        return list(d.values())

