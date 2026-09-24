class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, suffix, output = n*[1], n*[1], n*[1]
        prod = 1
        for i in range(1, n):
            prod = prod * nums[i-1]
            prefix[i] = prod
        prod = 1
        for i in range(n-2, -1, -1):
            prod = prod*nums[i+1]
            suffix[i] = prod
        for i in range(n):
            output[i] = prefix[i]*suffix[i]
        return output 

        
