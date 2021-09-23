# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 16:43:44 2021

@author: Arman
"""

import collections


# internet
def lengthOfLongestSubstring(self, s: str) -> int:
        self.res = 0
        dq = collections.deque()
        print(collections)
        for c in s:
            print(c)
            while c in dq:
                dq.popleft()
            
            dq.append(c)
            print(dq) 
            print('-----------------------')
            self.res = max(self.res, len(dq))
            
        return self.res
    
    
# mine
def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    q = collections.deque()
    max_len = 0
    for letter in s:
        if letter in q:
            while letter in q:
                q.popleft()
        q.append(letter)
        if len(q) > max_len:
            max_len = len(q)
    return max_len