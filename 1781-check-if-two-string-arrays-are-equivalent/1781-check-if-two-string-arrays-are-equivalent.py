class Solution:
    def arrayStringsAreEqual(self, s: List[str], t: List[str]) -> bool:
        s="".join(s)
        t="".join(t)
        if s==t:
            return True
        else:
            return False
        