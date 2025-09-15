class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        par={")":"(","}":"{","]":"[",}
        for i in s:
            if i in par.values():
                stack.append(i)
            elif not stack or par[i]!=stack.pop():
                return False
        return not stack

        