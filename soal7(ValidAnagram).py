# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h = {}
        # looing i ada pada s
        for i in s:
            h[i] = h.get(i, 0) + 1
        # looping j ada pada t
        for j in t:
            if h.get(j, 0) == 0:
                return False
            else:
                h[j] -= 1
        for k in h:
            if h[k] >= 1:
                return False
        return True