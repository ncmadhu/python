# Enter your code here. Read input from STDIN. Print output to STDOUT
test_num = int(raw_input().strip())
for i in range(test_num):
    string = str(raw_input().strip())
    count = 0
    for j in range(len(string) - 1):
        if string[j] == string[j + 1]:
            count += 1
    print count