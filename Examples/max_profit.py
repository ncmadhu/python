# Author: Madhu Chakravarthy
# Date: 04-07-2017

def max_profit(stock_price):

    day_min = stock_price[0]
    max_profit = stock_price[1] - day_min

    for i in range(len(stock_price)):

        if i == 0:
            continue

        diff = stock_price[i] - day_min

        if diff > max_profit:
            max_profit = diff

        if stock_price[i] < day_min:
            day_min = stock_price[i]


    print max_profit


if __name__ == "__main__":

    max_profit([10, 7, 5, 8, 11, 9])
    max_profit([10, 7, 5, 4, 1, 0])
