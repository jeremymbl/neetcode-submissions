class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # exemple : nums = [-1,0,1,2,-1,-4]
        n = len(nums)
        nums.sort()
        # nums = [-4, -1, -1, 0, 1, 2]
        res = []
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # on fait un two pointers sur le reste de la liste
            target = -nums[i]
            j = i+1
            k = n-1
            while j < k:
                somme = nums[j] + nums[k]
                if somme < target:
                    j += 1
                if somme > target:
                    k -= 1
                if somme == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j-1] == nums[j]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
        return res
