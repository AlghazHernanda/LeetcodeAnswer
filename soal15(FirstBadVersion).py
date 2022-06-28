# https://leetcode.com/problems/first-bad-version/
# https://programs.programmingoneonone.com/2021/09/leetcode-first-bad-version-problem-solution.html


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 0
        last = n
        while first <= last:
            mid = (first+last)//2
            if isBadVersion(mid):
                if not isBadVersion(mid-1):
                    return mid
                else:
                    last = mid - 1
            else:
                first = mid + 1
        
        return -1