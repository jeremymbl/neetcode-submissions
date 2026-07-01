class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # the idea is to create an "occurence tuple" for each word of strs
        # the tuple looks like this (n)_i for 0<=i<=25
        # where each element of the tuple is equal to n if the letter at index i 
        # of the alphabet is present n times in the word
        # for example, the tuple for cat is (1, 0, 1, ..., 0, 1, 0, 0, ..)
        # we'll create a hash where each key is that tuple and the values will be 
        # the list of strings which have this tuple
        d = dict()
        for word in strs:
            occ_list = [0]*26
            for char in word:
                occ_list[ord(char)-ord("a")] += 1
            occ_tuple = tuple(occ_list)
            if occ_tuple not in d:
                    d[occ_tuple] = []
                    d[occ_tuple].append(word)
            else:
                    d[occ_tuple].append(word)
        return list(d.values())