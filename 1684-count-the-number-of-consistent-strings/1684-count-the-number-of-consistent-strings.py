class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        for i in range(len(words)):
            if all(char in allowed for char in words[i]):
                count=count+1
        return count
        