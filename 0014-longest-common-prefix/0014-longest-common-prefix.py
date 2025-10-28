
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while s[:len(prefix)] != prefix and prefix:
                prefix = prefix[:-1]
            if not prefix:
                break
        return prefix
