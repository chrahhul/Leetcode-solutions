class Solution:
    def reverseDegree(self, s: str) -> int:
        res=0
        for i in range(len(s)):
             res+=(26-(ord(s[i])-97))*(i+1)
        return res
        