#Author: Madhu Chakravarthy
#Date: 31-08-2019

from nose.tools import assert_equal

class Solution(object):
    def is_substring(self, stringA, stringB):
        if stringA is None or stringB is None:
            return False

        lengthA = len(stringA)
        lengthB = len(stringB)
        
        if lengthA != lengthB:
            return False

        if lengthA == 0 and lengthB == 0:
            return True

        start = stringA[0]
        match = 0
        for char in stringB:
            if char == start:
                break
            else:
                match += 1

        return stringA == stringB[match:] + stringB[0:match]

if __name__ == "__main__":
    sol = Solution()
    assert_equal(sol.is_substring('o', 'oo'), False)
    assert_equal(sol.is_substring(None, 'foo'), False)
    assert_equal(sol.is_substring('', 'foo'), False)
    assert_equal(sol.is_substring('', ''), True)
    assert_equal(sol.is_substring('foobarbaz', 'barbazfoo'), True)
    print('Success: test_rotation')

