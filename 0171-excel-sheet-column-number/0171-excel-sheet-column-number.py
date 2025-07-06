class Solution:
    def titleToNumber(self, ct: str) -> int:
        res=0
        for i in ct:
            res=res*26+(ord(i)-ord("A")+1)
           
        return res    