def two_max(numbers):
  
  max1 = numbers[0]
  max2 = numbers[1]
  
  for num in numbers:
    if num > max1:
      max1 = num
    elif num > max2:
      max2 = num
    if max2 > max1:
      max1, max2 = max2, max1
  print max1
  print max2

if __name__ == "__main__":
  two_max([1,3,7,9,8])
  two_max([10,3,7,9,8])
