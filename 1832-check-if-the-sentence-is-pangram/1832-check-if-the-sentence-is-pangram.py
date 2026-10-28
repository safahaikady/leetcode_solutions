class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        c=set(sentence)
        return len(c)==26
        