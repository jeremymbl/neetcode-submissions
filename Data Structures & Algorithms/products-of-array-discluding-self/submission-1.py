class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # naive
        res = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            p = 1
            for j in range(i):
                p = p*nums[j]
            for j in range(i+1, len(nums)):
                p = p*nums[j]
            res[i] = p
        return res

