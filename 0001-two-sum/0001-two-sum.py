class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       hashs={}
       for i,num in enumerate(nums):
        if target-num in hashs:
            return[hashs[target-num],i]
        hashs[num]=i