class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a = 0
        b = 0
        result = []
        while a < len(word1) and b < len(word2):
            result.append(word1[a])
            result.append(word2[b])
            a += 1
            b += 1
        if len(word1) < len(word2):
            result.extend(word2[b:])
        else:
            result.extend(word1[a:])
        return "".join(result)
