class Solution:
    def strStr(self, hay: str, nee: str) -> int:
       
        for i in range(len(hay)):
            if hay[i:i+len(nee)]==nee:
                return i
        return -1
        
        