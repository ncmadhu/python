#Author: Madhu Chakravarthy
#Date: 04-05-2018
class Solution(object):
    def countAndSay(self, n):

        seq = '1'
        if n == 1:
            return seq
        seqCount = 2
        while seqCount <= n:
            numList = list(seq)
            length = len(numList)
            sequence = []
            count = 0
            i = 0
            while i < length:
                while i + 1 < length  and numList[i] == numList[i+1]:
                    count += 1
                    i += 1
                count += 1
                sequence.append([count, numList[i]])
                count = 0
                i += 1
            #print sequence
            seq = ''
            for elem in sequence:
                seq += str(elem[0]) + elem[1]
            seqCount += 1
        return seq

if __name__ == "__main__":
    sol = Solution()
    print sol.countAndSay(1)
    print sol.countAndSay(2)
    print sol.countAndSay(3)
    print sol.countAndSay(4)
    print sol.countAndSay(5)
    print sol.countAndSay(6)
