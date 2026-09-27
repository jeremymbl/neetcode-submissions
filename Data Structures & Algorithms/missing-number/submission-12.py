class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if 0 not in nums:
            return 0
        n = len(nums)
        somme = sum(nums)
        real_somme = n*(n+1)/2
        return int(real_somme-somme)