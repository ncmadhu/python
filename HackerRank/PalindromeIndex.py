# Enter your code here. Read input from STDIN. Print output to STDOUT
num_tests = int(raw_input().strip())
for i in range(num_tests):
    string = str(raw_input().strip())
    #print string
    rev_string = string[::-1]
    if string != rev_string:
        index = -1
        length =  len(string)
        half_length = length / 2
        #print half_length
        for i in range(half_length):
            if string[i] != rev_string[i]:
                if i <= half_length - 1:
                    new_str = string[0:i] + string[i + 1:]
                    alt_str = rev_string[0:i] + rev_string[i + 1:]
                else:
                    new_str = string[0:i]
                    alt_str = rev_string[0:i]
                rev_new_str = new_str[::-1]
                rev_alt_str = alt_str[::-1]
                if new_str == rev_new_str:
                    index = i
                    break
                elif alt_str == rev_alt_str:
                    #print i
                    index = length - 1 - i
                    break
                else:
                    index = -1
                    break
        print index
                
    else:
        print -1