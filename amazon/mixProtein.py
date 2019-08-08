#Author: Madhu Chakravarthy
#Date: 08-05-2018
class Solution(object):
    def mixProtein(self, n, string):
        length = len(string)
        strList = list(string)
        start = 0
        for i in range(n):
            curr = (start + 1) % length
            while curr != start:

                if curr == start:
                    break
