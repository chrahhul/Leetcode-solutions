class Solution:
    def strStr(self, hay: str, nee: str) -> int:
        if len(hay)<len(nee):
            return -1
        for i in range(len(hay)):
            if hay[i:i+len(nee)]==nee:
                return i
        return -1
        
        