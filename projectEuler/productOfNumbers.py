# Author: Madhu Chakravarthy
# Date: 07-06-2017

def productOfNumbers(list):

    result = []

    for i in range(len(list)):

        newList = list[0:i] + list[i+1:]
        result.append(reduce(lambda x,y: x * y, newList))

    return result




if __name__ == "__main__":

    print productOfNumbers([1,7,3,4])


        
