class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max1=0
        for i in range(len(accounts)):
            sum1=sum(accounts[i])
            if max1<sum1:
                max1=sum1
        return max1
        