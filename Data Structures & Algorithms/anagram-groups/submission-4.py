class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for word in strs:
            # pour chaque mot on construit un 26-uplet où chaque élément compte le nombre d'occurences de la lettre en question 
            # par exemple pour "act" on construit (1, 0, 1, ...., 1, 0, 0, ..)
            occ_list = [0]*26
            for char in word:
                i = ord(char) - ord("a")
                occ_list[i] += 1
            occ_tuple = tuple(occ_list)
            d[occ_tuple].append(word)
        return list(d.values())