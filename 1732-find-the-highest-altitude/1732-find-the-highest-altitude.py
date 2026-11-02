class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        ans=[0]
        for i in range(len(gain)):
            ans.append(sum(gain[:i+1]))
        return max(ans)
        