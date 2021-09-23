# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 17:24:54 2021

@author: Arman
"""

# internet
def increasingTriplet(self, nums):
    if len(nums) < 3:
        return False 
    N = len(nums)
    triplet_min = [float('inf')] * 3
    print(triplet_min)
    for i in range(0, N):
        if nums[i] <= triplet_min[0]:
            triplet_min[0] = nums[i]
        elif nums[i] <= triplet_min[1]:
            triplet_min[1] = nums[i]
        elif nums[i] <= triplet_min[2]:
            triplet_min[2] = nums[i]
            return True
        print(triplet_min)
    
    return False

# mine
def increasingTriplet(self, nums):
    res = [float('inf'), float('inf'), float('inf')]
    for x in nums:
        if x <= res[0]:
            res[0] = x
        elif x <= res[1]:
            res[1] = x
        elif x <= res[2]:
            res[2] = x
            return True
    return False