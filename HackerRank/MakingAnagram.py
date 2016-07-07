# Enter your code here. Read input from STDIN. Print output to STDOUT
str_1 = raw_input().strip()
str_2 = raw_input().strip()
set_all = set(str_1).union(set(str_2))
#print set_all
num_deletion = 0
for ch in set_all:
    num_deletion += max(0,str_1.count(ch) - str_2.count(ch))
    num_deletion += max(0,str_2.count(ch) - str_1.count(ch))
print num_deletion