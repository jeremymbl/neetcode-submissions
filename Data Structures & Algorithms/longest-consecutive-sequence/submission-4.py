class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for x in s: 
            if x-1 in s:
                continue
            res_temp = 1
            k = x+1
            while k in s:
                res_temp += 1
                k += 1
            res = max(res, res_temp)
            
        return res
        