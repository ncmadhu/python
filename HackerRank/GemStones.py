# Enter your code here. Read input from STDIN. Print output to STDOUT
num_rock = int(raw_input().strip())
rock_list = []
for i in range(num_rock):
    rock_list.append(list(str(raw_input().strip())))
rock_union_list = set().union(*rock_list)
count = 0
for ch in rock_union_list:
    is_present =  True
    for rock in rock_list:
        if ch not in rock:
            is_present = False
            break
    if is_present:
        count += 1
print count