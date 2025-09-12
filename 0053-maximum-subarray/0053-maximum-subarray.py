class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxs=curr=nums[0]
        for i in nums[1:]:
            curr=max(i,curr+i)
            maxs=max(curr,maxs)
        return maxs

        