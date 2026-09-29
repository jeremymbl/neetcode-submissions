class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # recherche dichotomique
        # le concept est simple : 
        # on regarde au milieu de la liste
        # si le target est plus grand, faut regarder à droite: on répète sur le milieu de la liste de droite
        # sinon pareil mais à gauche
        n = len(nums)
        l, r = 0, n-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid+1
            else:
                r = mid-1
        return -1
