# Enter your code here. Read input from STDIN. Print output to STDOUT
def calculate_num_operations(string):
    num_operations = 0
    if string == string[::-1]:
        return 0
    length = len(string)
    half_len = length / 2
    even_or_odd = length % 2
    if even_or_odd:
        left_half = string[0:half_len]
        right_half = string[half_len + 1 :]
        for i in range(len(left_half)):
            ch_l_ascii = ord(left_half[i])
            ch_r_ascii = ord(right_half[-1 -i])
            num_operations += max(ch_l_ascii,ch_r_ascii) -  min(ch_l_ascii,ch_r_ascii)
        return num_operations
    else:
        left_half = string[0:half_len]
        right_half = string[half_len :]
        for i in range(len(left_half)):
            ch_l_ascii = ord(left_half[i])
            ch_r_ascii = ord(right_half[-1 -i])
            num_operations += max(ch_l_ascii,ch_r_ascii) -  min(ch_l_ascii,ch_r_ascii)
        return num_operations