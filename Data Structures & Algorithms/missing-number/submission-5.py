class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        d = {i: False for i in range(n+1)}
        for i in range(n):
            d[nums[i]] = True
        res = next(k for k, v in d.items() if v is False)
        return res