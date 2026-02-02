class Solution(object):
    def countDigits(self, num):
        count = 0
        for i in str(num):
            n = int(i)
            if n != 0 and num % n == 0:
                count += 1
        return count
    
        