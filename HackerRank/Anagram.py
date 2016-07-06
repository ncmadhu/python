# Enter your code here. Read input from STDIN. Print output to STDOUT
num_test =  int(raw_input().strip())
for i in range(num_test):
    string = str(raw_input().strip())
    num_conversions = 0
    length = len(string)
    if length % 2 == 0:
        left_half = string[0:length / 2]
        #print left_half
        right_half = string[length / 2:]
        #print right_half
        right_ch = set(right_half)
        #print right_ch
        for ch in right_ch:
            count_r = right_half.count(ch)
            count_l = left_half.count(ch)
            if count_r > count_l:
                #print count_r - count_l
                # ch
                num_conversions += count_r - count_l
        print num_conversions            
    else:
        print -1