#Given an array of strings strs, group the anagrams together. 
#You can return the answer in any order

class Solution(object):
    def groupAnagrams(self, strs):

        d = defaultdict(list)   
        for word in strs:
            new_word = tuple(sorted(word))
            d[new_word].append(word)  
        
        return list(d.values())
        
