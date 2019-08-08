#Author: Madhu Chakravarthy
#Date: 19-04-2018

def maxProfit(prices):

    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit = profit + prices[i] - prices[i-1]
    return profit

if __name__ == "__main__":

    print maxProfit([1,2,4,2,5,6,1])



