# Author: Madhu Chakravarthy
# Date: 13-01-2018

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        profit = 0
        if length > 1:
            start = 0
            next = start + 1
            high = prices[start]
            while start < next and next < length:
                if prices[next] > prices[start] and prices[next] > high:
                    high = prices[next]
                    next += 1
                    if next >= length:
                        profit = profit + high - prices[start]
                    continue
                profit = profit + high - prices[start]
                start = next
                next = start + 1
                high =  prices[start]

        return profit

    def simpleSolution(self, prices):
        length = len(prices)
        profit = 0
        for i in range(1,length):
            if prices[i] > prices[i-1]:
                profit = profit + prices[i] - prices[i-1]
        return profit

if __name__ == "__main__":
    solution = Solution()
    prices = [1,2,4,2,5,6,1]
    print solution.maxProfit(prices)
    prices = [1,2,3]
    print solution.maxProfit(prices)
    prices = [1,1,1,1,1,1]
    print solution.maxProfit(prices)
    prices = [1,1,1,1,1,4]
    print solution.maxProfit(prices)
    prices = [4,1,2]
    print solution.maxProfit(prices)
    print solution.simpleSolution(prices)

