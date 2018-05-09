#Author: Madhu Chakravarthy
#Date: 07-05-2018
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        length = len(strs)

        prefix = ''
        start = 0

        while True:
            try:
                noMatch =  False
                for i in range(1, length):
                    if strs[0][start] != strs[i][start]:
                        noMatch = True
                        break
                if noMatch:
                    break
                prefix = prefix + strs[0][start]
                start += 1
            except Exception as e:
                break
        return prefix

if __name__ == "__main__":
    sol =  Solution()
    strs = ["flower","flow","flight"]
    print sol.longestCommonPrefix(strs)
    strs = ["flower","flow","flows"]
    print sol.longestCommonPrefix(strs)
    strs = ["dog","racecar","car"] 
    print sol.longestCommonPrefix(strs)


