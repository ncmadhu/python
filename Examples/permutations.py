# Author: Madhu Chakravarthy
# Date: 10-01-2018

def cycle(letters):
  
    length = len(letters)
    for i in range(length):
        sublist1 = letters[0:i]
        sublist2 = letters[i+1:length]
        sublist = sublist1 + sublist2 
        sublistLength = len(sublist)
        count = 0
        while count < sublistLength:
            print list(letters[i]) + sublist
            sublist = sublist[1:] + sublist[0:1]
            count += 1

if __name__ == "__main__":
    cycle(['a', 'b', 'c','d'])

