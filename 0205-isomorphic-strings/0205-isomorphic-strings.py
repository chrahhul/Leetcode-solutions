class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a={}
        b={}
        if len(s)!=len(t):
            return False
        for i in range(0,len(s)):
            if s[i] not in a:
                a[s[i]]=i
            if t[i] not in b:
                b[t[i]]=i
            if a[s[i]]!=b[t[i]]:
                return False
        return True

        

            