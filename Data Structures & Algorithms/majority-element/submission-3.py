class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        n = len(nums)
        for x in nums:
            seen[x] += 1
        for x in seen:
            if seen[x] > n//2:
                return x

