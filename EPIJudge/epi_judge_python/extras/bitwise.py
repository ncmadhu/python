#Author: Madhu Chakravarthy
#Date: 07-08-2019

def extras():
    print(str(bin(6)) + " & " + str(bin(4)) + " -> " + str(bin(6 & 4)))
    print(str(bin(1)) + " | " + str(bin(2)) + " -> " + str(bin(1 | 2)))
    print(str(bin(8)) + " >> " + str(1) + " -> " + str(bin(8 >> 1)))
    print(str(bin(-16)) + " >> " + str(2) + " -> " + str(bin(-16 >> 2)))
    print(str(bin(1)) + " << " + str(10) + " -> " + str(bin(1 << 10)))
    # ~ is bit wise complement operator where ~x = -x - 1 (Twos complement is inverted and again interpreted as twos complement)
    # 0 -> 0000 -> 1111 -> -8 + 4 + 2 + 1 -> -1 ( 0 - 1 = -1)
    print(bin(~5))
    print(str(bin(15)) + " ^ " + str(bin(10)) + " -> " + str(bin(15 ^ 10)))

if __name__ == "__main__":
    extras()