class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        milieu = (l+r)//2

        while l <= r:
            if nums[milieu] == target:
                return milieu
            elif nums[milieu] > target:
                r = milieu-1
            else:
                l = milieu+1
            milieu = (l+r)//2
        return -1
            

