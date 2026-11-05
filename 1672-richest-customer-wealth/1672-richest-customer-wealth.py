class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max=0
        for i in range(len(accounts)):
            sum1=0
            for j in range(len(accounts[i])):
                sum1+=accounts[i][j]
            if sum1>max:
                max=sum1
        return max
        