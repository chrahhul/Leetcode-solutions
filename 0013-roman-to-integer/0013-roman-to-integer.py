class Solution:
    def romanToInt(self, s: str) -> int:
        res=0
        Roman={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000

        }
        for a,b in zip(s,s[1:]):
            if Roman[a]<Roman[b]:
                res-=Roman[a]
            else:
                res+=Roman[a]
        return res+Roman[s[-1]]

        