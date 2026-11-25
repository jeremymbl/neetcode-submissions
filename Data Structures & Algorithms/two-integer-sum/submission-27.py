class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i, x in enumerate(nums):
            diff = target - x
            # is diff in seen? 
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[x] = i
        
        
