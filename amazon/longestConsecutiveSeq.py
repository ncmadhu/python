# Author: Madhu Chakravarthy
# Date: 07-02-2018

class Solution(object):
    def longestSeq(self, arr):
        numDict = {}
        for num in arr:
            numDict[num] = True
        longestSequence = []
        for num in numDict:
            if num - 1 in numDict:
                continue
            else:
                seq = [num]
                while True:
                    if num + 1 in numDict:
                        num += 1
                        seq.append(num)
                    else:
                        if len(seq) > len(longestSequence):
                            longestSequence = seq
                        break
        return longestSequence

if __name__ == "__main__":
    sol = Solution()
    arr = [2,1,6,9,4,3]
    print sol.longestSeq(arr)
    arr = [1,6,9,4,3,5,7,8]
    print sol.longestSeq(arr)
