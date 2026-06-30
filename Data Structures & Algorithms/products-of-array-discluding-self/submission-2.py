class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p1 = [1 for _ in range(n)]
        p = nums[0]
        for i in range(1, n):
            p1[i] = p*p1[i-1]
            p = nums[i]
        s1 = [1 for _ in range(n)]
        nums_reversed = nums.copy()
        nums_reversed.reverse()
        s = nums_reversed[0]
        for i in range(1, n):
            s1[i] = s*s1[i-1]
            s = nums_reversed[i]
        res = [1 for _ in range(n)]
        for i in range(n):
            res[i] = p1[i]*s1[n-1-i]
        return res
        
            