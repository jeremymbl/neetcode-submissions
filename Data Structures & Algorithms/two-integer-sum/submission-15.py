class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # redoing
        # we want x + y = t
        # so y = t - x
        # so we run through nums
        # for each x in nums, we look at the quantity y = t - x
        # and we ask ourselves if y is also an element of nums
        # so we store the quantity y in a hashmap
        # for eg with nums = [3,5,4,6] and target = 7
        # d = {}
        # i = 0, x = 3, y = 4 -> d is empty so ofc 4 isn't in it
        # so we just store (3:0) in the dict -> d = {3:0}
        # i = 1, x = 5, y = 2 -> 2 isn't in d
        # so we store (5, 1) in d -> d = {3:0, 5:1}
        # i = 2, x = 4, y = 3 -> 3 IS in d!
        # so we return the value associate with 3 which is 0 AND the index of 4
        # return [0, 2]
        d = dict()
        for (i, x) in enumerate(nums):
            diff = target - x
            if diff in d:
                return [ d[diff], i ]
            else:
                d[x] = i
        