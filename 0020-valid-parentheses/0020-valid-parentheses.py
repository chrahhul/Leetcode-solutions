class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        ma={
            ")":"(",
            "}":"{",
            "]":"["
        }
        for i in s:
            if i in ma.values():
                stack.append(i)
            elif i in ma.keys():
                if  not stack or ma[i]!=stack.pop():
                    return False
        return not stack


        