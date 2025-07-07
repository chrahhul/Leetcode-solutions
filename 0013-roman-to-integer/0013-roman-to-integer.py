class Solution:
    def romanToInt(self, s: str) -> int:
        res=0
        dic={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000

        }
        

        for a,b in zip(s,s[1:]):
            if dic[a] <dic[b]:
                res-=dic[a]
            else:
                res+=dic[a]
        return res+dic[s[-1]]