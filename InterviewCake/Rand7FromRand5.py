import unittest
import random
def rand5():
    return random.randrange(1,6)

def rand7():

    while True:
        roll1 = rand5()
        roll2 = rand5()
        outcome = (roll1 - 1) * 5 + (roll2 -1)
        if outcome > 21:
            continue
        else:
            return outcome % 7 + 1

if __name__ == "__main__":
    print(rand7())
    print(rand7())