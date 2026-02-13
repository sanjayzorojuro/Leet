class Solution(object):
    def differenceOfSums(self, n, m):
        n1 = []
        n2 = []
        i=1
        for i in range(n+1):
            if (i % m == 0):
                n1.append(i)
            else:
                n2.append(i)
        return sum(n2)-sum(n1)

       
        