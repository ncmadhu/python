#Author: Madhu Chakravarthy
#Date: 24-04-2018
class Solution(object):
    def strStr(self, haystack, needle):
        needleLen = len(needle)
        haystackLen = len(haystack)
        if needleLen == 0 and haystackLen == 0:
            return 0
        if needleLen == 0:
            return 0 
        if haystackLen == 0 or haystackLen < needleLen:
            return -1
        start = 0
        j = 0
        while start < haystackLen:
            i = start
            while haystack[i] != needle[j]:
                i += 1
                if i >= haystackLen:
                    return -1
            firstFoundIndex = i
            while j < needleLen and i < haystackLen:
                if haystack[i] == needle[j]:
                    i += 1
                    j += 1
                    """
                    if i >= haystackLen:
                        print i
                        return -1
                    """
                else:
                    break
            if j == needleLen:
                return firstFoundIndex
            elif i >= haystackLen:
                return -1
            else:
                j = 0
                start += 1

    def strStr2(self, haystack, needle):
        haystackLen = len(haystack)
        needleLen = len(needle)
        if haystackLen < needleLen:
            return -1
        if not needle:
            return 0
        i = j = 0
        while j < needleLen and i < haystackLen:
            if haystack[i] != needle[j]:
                i = i - j + 1
                j = 0
                continue
            i += 1
            j += 1

        return i - j if j == needleLen else -1


if __name__ == "__main__":
    sol =  Solution()
    print sol.strStr("hello", "ll")
    print sol.strStr("hello", "")
    print sol.strStr("", "ll")
    print sol.strStr("h", "ll")
    print sol.strStr("helloll", "ll")
    print sol.strStr("bbaa", "aab")
    print sol.strStr("b", "b")
    print sol.strStr("mississipi", "issip")
    print sol.strStr2("hello", "ll")
    print sol.strStr2("hello", "")
    print sol.strStr2("", "ll")
    print sol.strStr2("h", "ll")
    print sol.strStr2("helloll", "ll")
    print sol.strStr2("bbaa", "aab")
    print sol.strStr2("b", "b")
    print sol.strStr2("mississipi", "issip")


    
