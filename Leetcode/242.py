#Given two strings s and t, return true if t is an anagram of s, and false otherwise.

class Solution(object):
    def isAnagram(self, s, t):
        word1= Counter(s)
        word2= Counter(t)

        if len(word1) != len(word2):
            return False
        elif word1 == word2: 
            return True
        else: 
            return False 
