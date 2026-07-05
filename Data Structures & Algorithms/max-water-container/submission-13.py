class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i = 0
        j = n-1
        # l'aire d'un container est: (j-i)*min(heights[i], heights[j])
        res = 0
        while i < j:
            res = max(res, (j-i)*min(heights[i], heights[j]))
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return res 

            