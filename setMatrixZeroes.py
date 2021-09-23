# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 16:10:10 2021

@author: Arman
"""

# from internet, put in python 3 if needed
def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        
        # extract the indexes with 0
        for idx_r, row in enumerate(matrix):
            for idx_c, v in enumerate(row):
                if v == 0:
                    rows.add(idx_r)
                    cols.add(idx_c)
        print(matrix)
        print(rows)
        print(cols)
        
        # obfuscate rows
        for row in rows:
            for col in range(len(matrix[row])):
                matrix[row][col] = 0
        
        # obfuscate columns
        for col in cols:
            for row in range(len(matrix)):
                matrix[row][col] = 0
                
                
# mine
def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_track = set()
        col_track = set()
        for row_ind, row in enumerate(matrix):
            for col_ind, val in enumerate(row):
                if val == 0:
                    row_track.add(row_ind)
                    col_track.add(col_ind)
        for val in row_track:
            matrix[val] = [0 for x in range (len(matrix[0]))]
        
        for val in col_track:                                 
            for x in range(len(matrix)):
                matrix[x][val] = 0
                