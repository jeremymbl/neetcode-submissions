class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = defaultdict(bool)
        for x in nums:
            if seen[x]:
                return True
            else:
                seen[x] = True
        return False

