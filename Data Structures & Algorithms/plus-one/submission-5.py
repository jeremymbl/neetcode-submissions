class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # c'est hyper simple, faut pas trop penser en terme de maths (retenue etc)
        n = len(digits)
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        if digits[0] == 0:
            return [1] + digits
        return digits