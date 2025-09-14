class Solution:
    def isPalindrome(self, x):
        s = str(x)
        if s == s[::-1]:
            return True
        return False
x=121
ob=Solution()
print(ob.isPalindrome(x))


