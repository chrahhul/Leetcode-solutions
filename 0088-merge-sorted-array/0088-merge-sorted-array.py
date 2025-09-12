class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        res=[]
        nums=nums1[:m]
        nums2=nums2[:n]
        i,j=0,0
        while i<m and j<n:
            if nums[i]<nums2[j]:
                res.append(nums[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
        while i<m:
            res.append(nums[i])
            i+=1
        while j<n:
            res.append(nums2[j])
            j+=1
        for k in range(m+n):
            nums1[k]=res[k]