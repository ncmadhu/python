# Enter your code here. Read input from STDIN. Print output to STDOUT
num_tests = int(raw_input().strip())
for i in range(num_tests):
    str_a = str(raw_input().strip())
    str_b = str(raw_input().strip())
    set_a = set(str_a)
    set_b = set(str_b)
    is_present = 'NO'
    for ch in set_a:
        if ch in set_b:
            is_present = 'YES'
            break
    print is_present