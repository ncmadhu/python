#Author: Madhu Chakravarthy
#Date: 25-02-2018

class Solution(object):
    def longestIncreasingSubSequence(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        arrLen = len(arr)
        lenArr = [1] * arrLen
        seqArr = []
        for i in range(arrLen):
            seqArr.append(i)

        for i in range(1, arrLen):
            for j in range(0, i):
                if arr[i] > arr[j]:
                    if lenArr[j] + 1 > lenArr[i]:
                        lenArr[i] = lenArr[j] + 1
                        seqArr[i] = j

        maxIndex = 0

        for i in range(len(lenArr)):
            if lenArr[i] > lenArr[maxIndex]:
                maxIndex = i

        curIndex = maxIndex
        sequence = []

        while True:
            sequence.insert(0, arr[curIndex])
            if curIndex != seqArr[curIndex]:
                curIndex = seqArr[curIndex]
            else:
                break
        return sequence

if __name__ == "__main__":
    sol = Solution()
    arr = [0, -1, -2, 3, 6, 8, 5]
    print sol.longestIncreasingSubSequence(arr)
    arr = [-1, 0, 3, 6, 8, 5]
    print sol.longestIncreasingSubSequence(arr)
    arr = [-1, 0, 3, -5, 6, 8, 9]
    print sol.longestIncreasingSubSequence(arr)
