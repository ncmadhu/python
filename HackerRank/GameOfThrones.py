found = True
# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False
string = str(raw_input().strip())
length = len(string)
one_odd_ch =  False
str_len_odd = length % 2
set_str = set(string)
for ch in set_str:
    ch_count = string.count(ch)
    if str_len_odd:
        if ch_count % 2 and not one_odd_ch:
            one_odd_ch = True
        elif ch_count % 2:
            found = False
            break
    else:
        if ch_count % 2:
            found = False
            break

if not found:
    print("NO")
else:
    print("YES")
