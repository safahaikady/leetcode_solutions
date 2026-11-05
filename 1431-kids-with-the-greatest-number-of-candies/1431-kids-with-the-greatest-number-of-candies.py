class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_can=max(candies)
        ans=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies>=max_can:
                ans.append(True)
            else:
                ans.append(False)
        return ans
