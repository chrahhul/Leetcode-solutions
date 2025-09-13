class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num=set(nums)
        curr=0
        maxl=0
        for i in num:
            if i-1 not in num:
                curr=i
                c=1
                while  curr+1 in num:
                    curr+=1
                    c+=1
                maxl=max(c,maxl)
        return maxl

        