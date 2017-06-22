# Author: Madhu Chakravarthy
# Date: 21-06-2017
from itertools import combinations, chain

def powerset(n):
    
    sum = 0

    comb = list(chain(*[combinations(range(1,n+1), ni) for ni in range(1,n+1)]))
    for elem in comb:
        for i in elem:
            sum += i
    print sum

if __name__ == "__main__":

    powerset(3)
    powerset(4)

