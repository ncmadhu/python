# Author: Madhu Chakravarthy
# Date: 04-07-2017

def show_balances(daily_balances):

    n = 3
    last_n_days = daily_balances[-n:]

    for i in range(n - 1):

        print "daily balances on {0} days ago: {1}".format(n, last_n_days[i:i+2])
        n = n - 1


if __name__ == "__main__":


    show_balances([107.92, 108.67, 109.86, 110.15])
    show_balances([107.92, 108.67, 109.86, 110.15])
