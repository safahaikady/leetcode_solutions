class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        leftsum = 0
        ans = []

        for num in nums:
            rightsum = total - leftsum - num
            ans.append(abs(leftsum - rightsum))
            leftsum += num

        return ans