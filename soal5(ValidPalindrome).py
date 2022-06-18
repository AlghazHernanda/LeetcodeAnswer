# https://leetcode.com/problems/valid-palindrome/
# (ValidPalindrome)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower() # 소문자로 만들어준다. If not, ball과 BALL을 다른 문자로 인식.
        strs = collections.deque() # list보다 deque을 사용하는 것이 훨씬 빠르다.
        
        for char in s:
            if char.isalnum(): # is alphanumeric 함수로 알파벳 or 숫자인지 check!
                strs.append(char)
        
        s = ''.join(strs)
        
        return s == s[::-1] # 문자열 뒤집어서 비교. slicing을 사용하는것이 가장 빠름.