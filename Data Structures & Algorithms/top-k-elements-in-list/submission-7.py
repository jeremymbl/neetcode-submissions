class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        d = list(d.items())
        d.sort(key = lambda pair: pair[1], reverse = True)
        # we have to look at the k first elements of d
        res = []
        for i in range(k):
            res.append(d[i][0])
        return res