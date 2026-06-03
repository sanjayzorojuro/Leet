class Solution(object):
    def countKeyChanges(self, s):
        key = 0
        s = s.lower()


        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                key += 1
        return key