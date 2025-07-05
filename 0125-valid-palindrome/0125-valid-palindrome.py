class Solution:
    def isPalindrome(self, s: str) -> bool:
        lis=[]
        for i in s:
            if i.isalnum():
                lis.append(i.lower())
        return lis==lis[::-1]
