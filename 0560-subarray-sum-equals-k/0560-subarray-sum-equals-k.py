class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref=0
        count=0
        frq={0:1}
        for num in nums:
            pref+=num
            if  pref -k in frq:
                count+=frq[pref-k]
            frq[pref]=frq.get(pref,0)+1
        return count