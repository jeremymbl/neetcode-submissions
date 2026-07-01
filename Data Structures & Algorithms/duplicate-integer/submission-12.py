class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # most elegant solution
        # transform nums into a set -> we remove all duplicates
        # since we don't wanna know which num is duplicated 
        # and only wanna know if there IS a duplicate 
        # we just need to compare the size of set(nums) and nums
        return len(set(nums)) != len(nums)