# Enter your code here. Read input from STDIN. Print output to STDOUT
num_tests = int(raw_input().strip())
for i in range(num_tests):
    string = str(raw_input().strip())
    rev_string = string[::-1]
    is_funny = True
    for i in range(1,len(string)):
        diff = abs(ord(string[i]) - ord(string[i - 1]))
        rev_diff = abs(ord(rev_string[i]) - ord(rev_string[i - 1]))
        if diff != rev_diff:
            is_funny = False
            break
    if is_funny:
        print "Funny"
    else:
        print "Not Funny"