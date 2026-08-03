class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # x + y = target donc y = target - x
        d = dict()
        for i, x in enumerate(nums):
            diff = target - x # y
            if diff in d:
                return [d[diff], i]
            else:
                d[x] = i
        

