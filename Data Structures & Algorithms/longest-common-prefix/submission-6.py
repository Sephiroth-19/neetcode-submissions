class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for word in strs[1:]:
            limit = min(len(prefix), len(word))
            for i in range(limit):
                if prefix[i] != word[i]:
                    prefix = prefix[:i]
                    break
            prefix = prefix[:limit]                    
        return prefix

