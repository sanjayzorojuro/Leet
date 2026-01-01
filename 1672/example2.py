class Solution(object):
    def maximumWealth(self, accounts):
        maxwealth = 0
        for account in accounts:
            maxwealth = max(maxwealth, sum(account))

        return maxwealth 