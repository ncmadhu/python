#Author: Madhu Chakravarthy
#Date: 06-02-2018
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        oneToNineteen = ['One', 'Two', 'Three', 'Four', 'Five',
                         'Six', 'Seven', 'Eight', 'Nine', 'Ten',
                         'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
                         'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen',
                         'Nineteen']

        twentyToNinety = ['Twenty', 'Thirty', 'Forty', 'Fifty',
                          'Sixty', 'Seventy', 'Eighty', 'Ninety']

        def words(n):

            if n < 20:
                return oneToNineteen[n -1: n]
            elif n < 100:
                return [twentyToNinety[n/10 - 2]] + words(n%10)
            elif n < 1000:
                return [oneToNineteen[n/100 - 1]] + ['Hundred'] + words(n%100)
            for power, word in enumerate(('Thousand', 'Million', 'Billion'),1):
                if n < 1000**(power+1):
                    return words(n/1000**power) + [word] + words(n%1000**power)

        return " ".join(words(num)) or 'Zero'

if __name__ == "__main__":
    sol = Solution()
    num = 12
    print sol.numberToWords(num)
    num = 22
    print sol.numberToWords(num)
    num = 922
    print sol.numberToWords(num)
    num = 32768 
    print sol.numberToWords(num)
    num = 932768 
    print sol.numberToWords(num)
    num = 1932768 
    print sol.numberToWords(num)
