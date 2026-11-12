class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i=word.find(ch)
        reverse=word[0:i+1]
        return reverse[::-1]+word[i+1:]