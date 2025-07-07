class Solution:
    def convertToTitle(self, cn: int) -> str:
        res=""
        while cn>0:
            cn-=1
            res=chr(cn%26 +ord("A"))+res
            cn//=26
        return res