class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        mp={}
        res=0
        for i in range(len(s)):
            mp[s[i]]=i
        for i in range(len(t)):
            res+= abs(i-mp[t[i]])
        return res
    



        