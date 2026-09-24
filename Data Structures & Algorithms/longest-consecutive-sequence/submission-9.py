class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        temp = []
        res = 1
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                res += 1
            elif nums[i+1] - nums[i] == 0:
                continue
            else:
                temp.append(res)
                res = 1
        temp.append(res)
        if len(temp) > 0:
            return max(temp)
        else:
            return res
