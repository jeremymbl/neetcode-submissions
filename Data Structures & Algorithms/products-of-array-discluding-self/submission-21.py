class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = n*[1]
        prod = 1
        for i in range(1, n):
            prod = nums[i-1]*prod
            output[i] = prod
        prod = 1
        for i in range(n-2, -1, -1):
            prod = nums[i+1]*prod
            output[i] = output[i]*prod
        return output

        
