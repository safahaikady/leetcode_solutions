class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        max_1=-1
        for i in range(len(arr)-1,-1,-1):
            curr=arr[i]
            arr[i]=max_1
            max_1=max(max_1,curr)
        return arr
        