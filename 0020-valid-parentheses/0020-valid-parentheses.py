class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        par={
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for i in s:
            if i in par.values():
                st.append(i)
            elif i in par.keys():
                if not st or par[i]!=st.pop():
                    return False
        return not st
