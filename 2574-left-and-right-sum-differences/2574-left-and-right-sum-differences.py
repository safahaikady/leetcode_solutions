class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            leftsum=0
            rightsum=0
            leftsum=sum(nums[:i])
            rightsum=sum(nums[i+1:])
            ans.append(abs(leftsum-rightsum))
        return ans