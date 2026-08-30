class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        hashmap = {}
        for i in range(len(s)):
            hashmap[s[i]] = hashmap.get(s[i], 0) + 1
            hashmap[t[i]] = hashmap.get(t[i], 0) - 1
        for i in range(len(s)):
            if hashmap[s[i]] != 0: return False

        return True