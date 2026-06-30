class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def create_prefix(lst: List[int]):
            # input = [n0, ..., nd-1]
            # output = [1, n0, n0n1, ..., n0n1..nd-2]
            product = 1
            res = [1]*len(lst)
            for i in range(1, len(lst)):
                res[i] = product*lst[i-1]
                product = res[i]
            return res

        prefix_nums = create_prefix(nums)
        suffix_nums = create_prefix(list(reversed(nums)))
        result = [1]*len(nums)
        for i in range(len(nums)):
            result[i] = prefix_nums[i]*suffix_nums[len(nums)-1-i]
        return result
