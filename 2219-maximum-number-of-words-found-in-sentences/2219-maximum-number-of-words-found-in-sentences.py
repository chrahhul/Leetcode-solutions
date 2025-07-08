class Solution:
    def mostWordsFound(self, s: List[str]) -> int:
        count=0
        for i in s:
            m=len(i.split(" "))
            count=max(count,m)
        return count
        
        