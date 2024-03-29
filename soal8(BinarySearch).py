# https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.helper(nums, 0, len(nums)-1, target)
    def helper(self, nums, l, r, target):
        # jika kira lebih besar dari kanan
        if l > r:
            return -1
        
        # jika kiri sama dengan kanan
        if l == r:
            # jika num[l] == target
            if nums[l] == target:
                # maka return 1
                return l
            return -1
        
        # rumus mid
        mid = (l+r) // 2
        # jika mid sama dengan target
        if nums[mid] == target:
            return mid
        # jika mid lebih besar dari target
        elif nums[mid] > target:
            return self.helper(nums, l, mid-1, target)
        # kalo lebih kecil
        else:
            return self.helper(nums, mid+1, r, target)