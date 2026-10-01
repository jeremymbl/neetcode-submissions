class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0
        nums_set = set(nums)
        for x in nums_set:
            if x-1 in nums_set:
                continue
            count = 1
            y = x+1
            while y in nums_set:
                y += 1
                count += 1
            best = max(best, count)
        return best