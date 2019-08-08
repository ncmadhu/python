#Auhtor: Madhu Chakravarthy
#Date: 1-03-2018
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: void modify string in place
        """

        length = len(s)
        start = 0
        i = 0
        while i < length:
            while i < length and s[i] != " ":
                i += 1
            self.reverse(s, start, i)
            i += 1
            start = i
        self.reverse(s, 0, length)
        print s

    def reverse(self, s, start, right):
        middle = (start + right) / 2
        for i in range(start, middle):
            right -= 1
            s[i], s[right] = s[right], s[i] 


if __name__ == "__main__":
    sol =  Solution()
    s = 'the sky is blue'
    sol.reverseWords(list(s))



