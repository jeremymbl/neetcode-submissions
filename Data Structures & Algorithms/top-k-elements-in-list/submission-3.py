class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # grouping numbers based on their frequency
        # pour nums = [2, 3, 1, 1, 9, 8, 1, 7, 2, 7, 8, 8, 8]
        # on reconstruit d = {2: 2, 3: 1, 1: 3, 9: 1, 8: 4, 7: 2]
        d = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)]
        for x in d:
            freq[d[x]].append(x)
        # freq = [[], [3, 9], [2, 7], [1], [8], [], [], [], [], [], [], [], [], []]
        # donc là on sait que 3 et 9 apparaissent 1 fois, 2 et 7 apparaissent 2 fois, 1 apparait 3 fois et 8 apparait 4 fois
        # donc la solution est [1, 8]
        res = []
        for bucket in reversed(freq):
            for x in bucket:
                res.append(x)
                if len(res) == k:
                    return res


            

        