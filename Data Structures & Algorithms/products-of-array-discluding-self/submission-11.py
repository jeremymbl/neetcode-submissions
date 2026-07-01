class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # redoing it for practice
        d = len(nums)
        res = [0 for _ in range(d)]
        product = 1
        for i in range(d):
            res[i] = product
            product *= nums[i]
        product = 1
        for i in range(d):
            res[d-1-i] *= product
            product *= nums[d-1-i]
        return res