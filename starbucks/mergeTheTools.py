#Author: Madhu Chakravarthy
#Date: 15-05-2018
def merge_the_tools(string, k):
    
    count = 0
    chrSet = []
    for char in string:
        if count < k:
            if char not in chrSet:
                chrSet.append(char)
            count += 1
        else:
            print "".join(chrSet)
            count = 1
            chrSet = [char]
    if chrSet:
        print "".join(chrSet)

if __name__ == "__main__":
    string = 'AABCAAADA'
    k = 3
    merge_the_tools(string, k)
