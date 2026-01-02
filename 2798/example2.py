class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        return len([x for x in hours if x >= target]) 