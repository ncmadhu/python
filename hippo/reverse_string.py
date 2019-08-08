#Author: Madhu Chakravarthy
#Date: 31-08-2019

class Solution(object):
    def reverse(self, string):
        if string is None:
            return string
        length = len(string)
        rev_str = list(string)
        if length < 2:
            return string
        for i in range(length / 2):
            rev_str[i], rev_str[length - 1 - i] = rev_str[length - 1 - i], rev_str[i]
        return rev_str

if __name__ == "__main__":
    sol = Solution()
    print sol.reverse("abba")
    print sol.reverse("abcd")
    print sol.reverse("edcba")
    print sol.reverse("ef")
    print sol.reverse("foo bar")
