class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_no=max(nums)
        c=0
        for i in range(len(nums)):
            c+=max_no-nums[i]
        return c
