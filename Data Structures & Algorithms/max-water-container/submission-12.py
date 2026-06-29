class Solution:
    def maxArea(self, heights: List[int]) -> int:
        import numpy as np
        n = len(heights)
        mat = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                mat[i,j] = abs(i-j)*min(heights[i], heights[j])
        return int(np.max(mat))