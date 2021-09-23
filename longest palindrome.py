# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 17:08:43 2021

@author: Arman
"""

def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        elif len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        else:
            start = 0
            end = 0
            res = ""
            for i in range(len(s)):
                opt1 = self.count_palindrome(s,i,i)
                opt2 = self.count_palindrome(s,i,i+1)
                opt3 = max(opt1,opt2)
                if opt3 > end - start:
                    start = i - ((opt3-1)//2)
                    end = i + ((opt3)//2)
            return s[start:end+1]
        
def count_palindrome(self, s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1


# mine
class Solution(object):
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        cur = ""
        
        if len(s) < 2:
            return s[0]
        elif len(s) == 2:
            return s[0] if s[0] != s[1] else s
        else:
            for i in range(len(s)):
                # can either start bab
                opt1 = palindromeHelper(s, i, i)
                # or baab
                opt2 = ""
                if i!= len(s) - 1 and s[i] == s[i+1]:
                    opt2 = palindromeHelper(s, i, i+1) 
                opt3 = opt1 if len(opt1) > len(opt2) else opt2
                if len(opt3)> len (cur):
                    cur = opt3
        return cur
    
     
# returns the palindrome starting at left and right indices
def palindromeHelper(s, left, right):
    substr = ""
    while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
        substr = s[left: right + 1]
        left -= 1
        right += 1
    return substr
    