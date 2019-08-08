#Author: Madhu Chakravarthy
#29-07-2019
class Solution(object):
    def __int__(self):
        print "Calculating max profit"

    def maxProfit(self, prices):
        size = len(prices)
        profit = 0
        for i in range(1, size):
            if prices[i] > prices[i-1]:
                profit = profit + prices[i] -prices[i-1]
        return profit

if __name__ == "__main__":
    Sol =  Solution()
    print Sol.maxProfit([1,2,4,2,5,6,1])

