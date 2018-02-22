#Author: Madhu Chakravarthy
#Date: 08-02-2018
class Solution(object):
    def getOddItem(self, arr):
        itemCounter = {}
        for item in arr:
            itemCounter[item] = itemCounter.get(item, 0) + 1

        for item, value in itemCounter.iteritems():
            if value % 2:
                return item

        return None

if __name__ == "__main__":
    sol = Solution()
    arr = [1,4,6,4,1]
    print sol.getOddItem(arr)

