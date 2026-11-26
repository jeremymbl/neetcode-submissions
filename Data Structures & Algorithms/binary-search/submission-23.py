class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            middle = (l+r)//2
            middle_element = nums[middle]
            if middle_element < target:
                l = middle+1
            elif middle_element > target:
                r = middle-1
            else:
                return middle
        return -1

            