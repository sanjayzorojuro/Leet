class Solution(object):
    def sumOfMultiples(self, n):
        arr=[]
        i=1
        while i <= n :
            if i%5==0 or i%3==0 or i%7==0:
                arr.append(i)
            i+=1
        return sum(arr)


n=int(input("Enter a number:"))
ob1=Solution()
print(ob1.sumOfMultiples(n))

        