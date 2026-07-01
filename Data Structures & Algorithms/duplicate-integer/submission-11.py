class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # redoing it to consolidate
        # with a hash
        seen = dict()
        for x in nums:
            # if x is in seen then we return True
            if x in seen:
                return True
            else:
                seen[x] = True
        return False