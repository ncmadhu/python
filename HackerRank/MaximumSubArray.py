# Enter your code here. Read input from STDIN. Print output to STDOUT

def max_sub_array(arr):
    max_now = arr[0]
    max_history = arr[0]
    max_non_contig = arr[0]

    for i in arr[1:]:
        max_now = max(i, max_now + i)
        max_history = max(max_history, max_now)        
        max_non_contig = max([max_non_contig, max_non_contig + i, i])  
    return str(max_history) + " " + str(max_non_contig)

t = int(raw_input().strip())
for i in range(t):
    n = int(raw_input().strip())
    array = map(int,raw_input().strip().split(" "))
    print max_sub_array(array)