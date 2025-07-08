class Solution:
    def maxFreqSum(self, s: str) -> int:
        lst=Counter(s)
        v=["a","e","i","o","u"]
        val=0
        ma=0
        for i in s:
            if i in v:
                val=max(val,lst[i])
            else:
                ma=max(ma,lst[i])
        return val+ma
        
