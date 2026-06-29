class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # naive solution 
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if j == i:
                    continue
                else:
                    if nums[i] + nums[j] == target:
                        return [i, j]
        

        