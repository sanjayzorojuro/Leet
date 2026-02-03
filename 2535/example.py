class Solution(object):
    def differenceOfSum(self, nums):
        ele = sum(nums)
        digitsum = 0
        for num in nums:
            for digit in str(num):
                digitsum += int(digit)
        return ele - digitsum
