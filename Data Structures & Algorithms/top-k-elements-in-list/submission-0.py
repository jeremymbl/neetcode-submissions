class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        for x in nums:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        l = list(d.items())
        # pour nums = nums = [2, 3, 1, 1, 9, 8, 1, 7, 2, 7, 8, 8, 8]
        # on aura l = [(2, 2), (3, 1), (1, 3), (9, 1), (8, 4), (7, 2)]
        # maintenant, on trie l selon la fréquence (donc selon le 2e élément de chaque couple)
        # on aura l = [(3, 1), (9, 1), (2, 2), (7, 2), (1, 3), (8, 4)]
        # et à la fin on renvoie les k dernières clés: si k = 2, on renvoie donc [1, 8]
        l = sorted(l, key=lambda pair: pair[1])
        return([t[0] for t in l[-k:]])
        
        