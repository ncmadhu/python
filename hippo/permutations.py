#Author: Madhu Chakravarthy
#Date: 31-08-2019
from collections import defaultdict

class Solution(object):

    def check_permutation(self, stringA, stringB):
        if stringA is None or stringB is None:
            return False
        if len(stringA) != len(stringB):
            return False

        unique_countA = defaultdict(int)
        unique_countB = defaultdict(int)

        for char in stringA:
            unique_countA[char] += 1

        for char in stringB:
            unique_countB[char] += 1

        return unique_countA == unique_countB

if __name__ == "__main__":
    sol = Solution()
    print sol.check_permutation("", "foo")
    print sol.check_permutation(None, "")
    print sol.check_permutation("", "")
    print sol.check_permutation("nib", "bin")
    print sol.check_permutation("AbC", "CbA")
    print sol.check_permutation("c at", "atc ")
