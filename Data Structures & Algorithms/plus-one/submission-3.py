class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        if digits[-1] < 9:
            digits[-1] += 1
        else:
            digits[-1] = 0
            retenue = 1
            for i in range(n-2, -1, -1):
                if digits[i] < 9:
                    digits[i] += retenue
                    retenue = 0
                else:
                    if retenue > 0:
                        digits[i] = 0
        if digits[0] == 0:
            return [1] + digits
        return digits
