class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for x in s: # test every start possible
            res_temp = 1
            k = x+1
            while k in s:
                res_temp += 1
                k += 1
            res = max(res, res_temp)
            
        return res
        