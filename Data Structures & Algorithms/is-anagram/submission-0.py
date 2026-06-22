class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_seen = {}
        t_seen = {}
        for x in s:
            if x in s_seen:
                s_seen[x] += 1
            else:
                s_seen[x] = 1

        for x in t:
            if x in t_seen:
                t_seen[x] += 1
            else:
                t_seen[x] = 1

        return s_seen == t_seen


        