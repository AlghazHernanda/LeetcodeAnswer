# https://leetcode.com/problems/longest-palindrome/
# https://programs.programmingoneonone.com/2021/10/leetcode-longest-palindrome-problem-solution.html

class Solution:
    def longestPalindrome(self, s: str) -> int:
        a = set()
        # jika l ada pada s
        for l in s:
            # jika l tidak ada di a
            if l not in a:
                a.add(l)
            # jalankan jika l ada di a
            else:
                a.remove(l)
        return len(s) - len(a) + 1 if len(a) else len(s)