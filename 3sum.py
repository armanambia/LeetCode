# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 15:22:16 2021

@author: Arman
"""

# from internet
def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        n = len(nums)
        r = n -1
        l = 0
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            num = nums[i]
            l = i + 1
            r = n - 1
            while l < r:
                total = num + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res
    

# my version
def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        # print(nums)
        for l in range(len(nums) -2):
            # going to need l, m, e
            cur = nums[l]
            m = l + 1
            e = len(nums) - 1
            while m != e:
                    second = nums[m]
                    last = nums[e]
                    total = cur + second + last
                    if total > 0:
                        
                        e -= 1
                    elif total < 0:
                        m += 1
                    else:
                        if([cur,second,last] not in res):
                            res.append([cur,second,last])
                        m += 1
        return res