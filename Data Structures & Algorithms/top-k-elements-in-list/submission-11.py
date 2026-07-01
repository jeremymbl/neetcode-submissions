class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # grouping numbers based on their frequency
        freq = [[] for _ in range(len(nums)+1)]
        for x in Counter(nums):
            freq[Counter(nums)[x]].append(x)
        res = []
        freq.reverse()
        count = 0 # we need to make sure 
        i = 0
        while i < len(freq) and count != k:
            if freq[i] == []:
                i += 1
            else:
                j = 0
                while j < len(freq[i]) and count <= k:
                    res.append(freq[i][j])
                    j += 1
                    count += 1
                i += 1
        return res

            
                


