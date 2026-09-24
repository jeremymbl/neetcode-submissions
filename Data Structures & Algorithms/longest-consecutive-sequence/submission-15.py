class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        ensemble = set(nums)
        for x in ensemble:
            if x-1 in ensemble:
                continue
            temp_x = 1
            y = x
            while y+1 in ensemble:
                temp_x += 1
                y += 1
            res = max(res, temp_x)
        return res