#Author: Madhu Chakravarthy
#Date: 20-03-2018
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """

        start =  0
        end = len(letters)

        index =  self.findPivot(letters, start, end, target)
        return letters[index % len(letters)]



    def findPivot(self, letters, start, end, target):

        while start < end:
            mid =  (start + end) / 2
            if letters[mid] <= target:
                start = mid+1
            else:
                end = mid

        return start


if __name__ == "__main__":
    sol = Solution()
    letters = ["c", "f", "j"]
    target = "a"
    print sol.nextGreatestLetter(letters, target)
    letters = ["c", "f", "j"]
    target = "c"
    print sol.nextGreatestLetter(letters, target)
    letters = ["c", "f", "j"]
    target = "d"
    print sol.nextGreatestLetter(letters, target)
    letters = ["c", "f", "j"]
    target = "g"
    print sol.nextGreatestLetter(letters, target)
    letters = ["c", "f", "j"]
    target = "j"
    print sol.nextGreatestLetter(letters, target)
    letters = ["c", "f", "j"]
    target = "k"
    print sol.nextGreatestLetter(letters, target)

