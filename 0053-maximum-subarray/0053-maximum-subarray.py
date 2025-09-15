class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxs=nums[0]
        x=nums[0]
        for i in nums[1:]:
            x=max(i,x+i)
            maxs=max(maxs,x)
        return maxs
        