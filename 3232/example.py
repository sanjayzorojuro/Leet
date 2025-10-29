class Solution(object):
    def canAliceWin(self, nums):
        s=[x for x in nums if x<10]
        d=[x for x in nums if x>=10]

        return True if sum(s) != sum (d) else False
        
