#Author: Madhu Chakravarthy
#Date: 17-05-2018
def makeChange(cost, amountGiven):
    
    change = amountGiven - cost
    print "Balance: %s" % change
    if change < 0:
        print [0,0,0,0,0]
        return
    changeList = str(change).split('.')
    if change >= 1.0:
        dollar = int(changeList.pop(0))
    else:
        dollar = 0
        
    quarters = int(changeList[0]) / 25
    balance = int(changeList[0]) % 25
    dimes = balance / 10
    balance = balance % 10
    nickels = balance / 5
    pennies = balance % 5
    print [dollar, quarters, dimes, nickels, pennies]

if __name__ == "__main__":
    makeChange(0.01, 5.00)
    makeChange(0.99, 5.00) #[4, 0, 0, 0, 1]
    makeChange(0.00, 1.41) #[1, 1, 1, 1, 1]
    makeChange(1.18, 4.25) #[3, 0, 0, 1, 2]
    makeChange(1.54, 0.00) #[0, 0, 0, 0, 0]
