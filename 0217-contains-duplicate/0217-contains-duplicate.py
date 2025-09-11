class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num=Counter(nums)
        for val,freq in num.items():
            if freq>=2:
                return True
        return False
        