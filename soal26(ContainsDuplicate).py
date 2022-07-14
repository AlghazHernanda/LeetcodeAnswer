# https://leetcode.com/problems/contains-duplicate/

class Solution(object):
    def containsDuplicate(self, nums):
        s = set()
        for num in nums:
            if num not in s:
                s.add(num)
            else:
                return True

        return False