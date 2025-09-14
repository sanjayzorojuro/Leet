class Solution(object):
    def mySqrt(self, x):
        if x == 0:
            return 0
        
        l , r = 1 , x
        ans = 0

        while l <= r:
            mid = l + (r - l) // 2
            m = mid * mid

            if m == x:
                return mid
            elif m < x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

                
        return ans
    
ob1=Solution()
ob1.mySqrt(8)

        