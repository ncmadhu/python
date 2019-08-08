#Author: Madhu Chakravarthy
#Date: 08-02-2018
class Solution(object):
    def getKFrequentItems(self, arr, k):
        arrLength = len(arr)
        countList = [None] * (arrLength + 1)
        freqMap = {}
        for item in arr:
            freqMap[item] = freqMap.get(item, 0) + 1
        for item, val in freqMap.iteritems():
            if countList[val]:
                countList[val].append(item)
            else:
                countList[val] = [item]

        kitems = []
        pos = len(countList) - 1
        while len(kitems) < k and pos >= 0:
            if countList[pos]:
                kitems.extend(countList[pos])
            pos -= 1
        return kitems

if __name__ == "__main__":
    sol = Solution()
    arr = [1,6,2,1,6,1,6]
    k = 2
    print sol.getKFrequentItems(arr, k)
    arr = [1,6,2,1,6,1,6,7,7,7,3,3,2,11]
    k = 5
    print sol.getKFrequentItems(arr, k)
