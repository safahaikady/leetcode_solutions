class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        res=s.split()
        ans=[]
        for i in range(k):
            ans.append(res[i])
        return ' '.join(ans)
        