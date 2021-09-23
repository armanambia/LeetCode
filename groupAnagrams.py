# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 16:42:50 2021

@author: Arman
"""

# internet
'''
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>> mp;
        int n = strs.size();
        for (int i = 0; i < n; i++){
            string s = strs[i];
            sort(s.begin(), s.end());
            mp[s].push_back(strs[i]);
        }
        vector<vector<string>> v;
        for(auto a: mp){
            v.push_back(a.second);
        }
        return v;
    }
};

'''


# mine
def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sorted_map = {}
        for val in strs:
            key = ''.join(sorted(val))
            if key not in sorted_map:
                sorted_map[key] = [val]
            else:
                sorted_map[key].append(val)
        
        return(sorted_map.values())