#Author: Madhu Chakravarthy
#Date: 27-02-2018
class Solution(object):
    def permutate(self, string):
        """
        :type string: String
        :rtype List[String]
        """
        #calculate length of given string
        length = len(string)

        #Initialize left and right edge
        left = 0
        right = length - 1

        #call permutate util
        combinations = self.permutateUtil(list(string), left, right)

    def permutateUtil(self, string, left, right):

        #check we reached right edge of the string
        #if reached return
        if left == right:
            self.printString(string)
        else:
            for i in range(left, right+1):
                #Swap left element with ith element and call
                #permutate again by moving to left one step
                string[left], string[i] = string[i], string[left]
                self.permutateUtil(string, left + 1, right)
                #restore original string by backtracking
                string[left], string[i] = string[i], string[left]

    def printString(self, string):
        print "".join(string)

if __name__ == "__main__":
    sol = Solution()
    string = 'ABC'
    sol.permutate(string)


