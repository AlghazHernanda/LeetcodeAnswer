# https://leetcode.com/problems/permutations/submissions/
# https://medium.com/coding-memo/leetcode-permutations-87fe41c9fa32

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []        
        # nums is decreased
        
        # slow
        # def h(arr, nums):
        #     n = len(nums)
        #     if n==1:
        #         arr.append(nums[0])
        #         res.append(arr.copy())
        #         arr.pop()
        #         return            
        #     for i in range(n):
        #         arr.append(nums[i])
        #         h(arr, nums[:i]+nums[i+1:]) # create new list O(n)
        #         arr.pop()
        #     # time: O(n!*n)
        # h([], nums)
        
        # efficient
        def h(i, arr, nums): # i represents new starting point and not going back
            n = len(nums)
            if i==n-1:
                arr.append(nums[i])
                res.append(arr.copy())
                arr.pop()
                return     
            # use i to forward the recursion
                # to make the starting point different so the sequence is shuffled
                    # swap i with each position in nums
            for j in range(i, n): 
                nums[i], nums[j] = nums[j], nums[i]
                # i now becomes j
                arr.append(nums[i]) # actually push j to arr
                # ready to forward
                h(i+1, arr, nums)
                arr.pop()
                # j is new and to be pushed in each round of traversal
                nums[i], nums[j] = nums[j], nums[i] # i needs to back to old position
                # so will not mess sequence, the j to be pushed is surely new
            # time: O(n!*n)        
        h(0, [], nums)
        
        return res