# https://leetcode.com/problems/majority-element/submissions/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums)-1)
    def helper(self, nums, l, r):

        # jika l == r maka jalankan if ini
        if l == r:
            return nums[l]
        
        # cari mid adalah kanan tambah kiri bagi 2
        mid = (l+r) // 2
        # kiri
        lm = self.helper(nums, l, mid)
        # kanan
        rm = self.helper(nums, mid+1, r)
        if lm == rm:
            return lm
        else:
            lc = sum([1 for i in range(l, r+1) if nums[i] == lm])
            rc = sum([1 for i in range(l, r+1) if nums[i] == rm])

            mid = (l+r) // 2
        lm = self.helper(nums, l, mid)
        rm = self.helper(nums, mid+1, r)

    
            if lc > rc:
                return lm
            return rm