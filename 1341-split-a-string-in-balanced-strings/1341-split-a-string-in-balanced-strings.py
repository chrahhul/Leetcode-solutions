class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res=0
        bal=0
        for i in s:
            if i=="R":
                bal+=1
            else:
                bal-=1
            if bal==0:
                res+=1
        return res
        