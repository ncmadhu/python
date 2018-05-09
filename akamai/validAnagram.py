#Author: Madhu Chakravarthy
#Date: 24-04-2018
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        return s == t
        


if __name__ == "__main__":
    sol = Solution()
    print sol.isAnagram("anagram", "nagaram")
    print sol.isAnagram("nagram", "nagaram")
