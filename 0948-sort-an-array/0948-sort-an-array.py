class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # base case
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2  # just split in half
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        # merge left and right
        i = j = 0
        merged = []

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged
