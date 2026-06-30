class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        d = len(nums)
        res = [1]*d
        for i in range(d):
            res[i] = product
            product *= nums[i]
        
        # res est maintenant la liste des préfixes
        
        product = 1
        for i in range(d-1, -1, -1):
            # on calcule les suffixes et on les multiplie direct aux préfixes
            res[i] *= product
            product *= nums[i]
        
        return res
            
            
            

            