class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        nums1=sorted(nums)
        return (nums1[-1]-1)*(nums1[-2]-1)
        