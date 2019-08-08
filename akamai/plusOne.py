#Author: Madhu Chakravarthy
#Date: 22-04-2018
class Solution(object):
    def plusOne(self, digits):
        sum = 0
        for num in digits:
            sum = (sum * 10) + num
        sum += 1
        newDigits = []
        while sum > 0:
            newDigits.insert(0, sum % 10)
            sum = sum / 10

        return newDigits

if __name__ == "__main__":
    sol =  Solution()
    print sol.plusOne([4,3,2])
