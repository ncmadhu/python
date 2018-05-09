#Author: Madhu Chakravarthy
#Date: 24-04-2018
def stringAddition(string):
  
  stringList = list(string)
  
  prevSign = 1
  
  if stringList[0] in ['-', '+']:
    if stringList[0] == '-':
      prevSign = -1
    stringList.pop(0)
  
  sum = 0
  stringLength = len(stringList)
  i = 0
  j = 0
  while i < stringLength:
    if stringList[i] not in ['-', '+']:
      i += 1
      continue
    numString = "".join(stringList[j:i])
    sum = sum + prevSign * float(numString)
    prevSign = -1 if stringList[i] == '-' else 1
    i += 1
    j = i
  numString = "".join(stringList[j:i])
  sum  = sum + prevSign * float(numString)
  return sum

if __name__ == "__main__":

    inputString="2.3+1.2-0.4+5.2"
    print stringAddition(inputString)
    inputString = "-8.3+2.4+3.6+10.0"
    print stringAddition(inputString)
