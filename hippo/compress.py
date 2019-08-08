#Author: Madhu Chakravarthy
#Date: 31-07-2019

class Solution(object):
    def compress(self, input):
        if input is None or not input:
            return input
        compressed = ""
        count = 0
        prev_char = input[0]
        for char in input:
            if char == prev_char:
                count += 1
            else:
                compressed = compressed + self.get_compressed_string(prev_char, count)
                prev_char = char
                count = 1
        compressed = compressed + self.get_compressed_string(prev_char, count)
        
        return compressed if len(compressed) < len(input) else input

    def get_compressed_string(self, char, count):
        return char + str(count) if count > 1 else char

if __name__ == "__main__":
    sol = Solution()
    print sol.compress('AABBCC')
    print sol.compress('AAABCCDDDDE')




