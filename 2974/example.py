class Solution(object):
    def numberGame(self, nums):
        res=[]
        i=0
        while nums:
            a=min(nums)
            nums.remove(a)
            b=min(nums)
            nums.remove(b)
            res.extend((b,a))
        return res