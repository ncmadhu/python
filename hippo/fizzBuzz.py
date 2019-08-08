#Author: Madhu Chakravarthy
#Date: 31-08-2019

class Solution(object):
    def fizz_buzz(self, num):
        if num is None or num < 1:
            raise Exception("Provide a valid number greater than 0")
        result = []
        for i in range(1, num+1):
            if i % 3 and i % 5:
                result.append(i)
            elif not i % 3 and not i% 5:
                result.append("FizzBuzz")
            elif i % 3:
                result.append("Buzz")
            else:
                result.append("Fizz")
        return result

if __name__ == "__main__":
    sol = Solution()
    print sol.fizz_buzz(15)
