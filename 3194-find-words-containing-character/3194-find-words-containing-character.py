class Solution:
    def findWordsContaining(self, s: List[str], x: str) -> List[int]:
        lst=[]
        for i in range(len(s)):
            if x in s[i]:
                lst.append(i)
        return lst
            


        