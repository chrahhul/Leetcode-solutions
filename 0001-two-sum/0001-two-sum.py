class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashs={}
        for i,ch in enumerate(nums):
            if target-ch in hashs:
                return[hashs[target-ch],i]
            hashs[ch]=i
        