# Enter your code here. Read input from STDIN. Print output to STDOUT
def string_replacement(string, length):

    max_char_count =  length / 4
    A_delta = string.count('A') - max_char_count
    #print A_delta
    C_delta = string.count('C') - max_char_count
    #print C_delta
    G_delta = string.count('G') - max_char_count
    #print G_delta
    T_delta = string.count('T') - max_char_count
    #print T_delta
    
    if A_delta == 0 and C_delta == 0 and G_delta == 0 and T_delta == 0:
        return 0
     
    min_sub = length
    head = 0
    tail = 0 
    
    while head < length:
        char_head = string[head]
        #print "char_head: " + char_head
        head += 1
        if char_head == 'A':
            A_delta -= 1
        elif char_head == 'C':
            C_delta -= 1
        elif char_head == 'G':
            G_delta -= 1
        elif char_head == 'T':
            T_delta -= 1
            
        while (A_delta <= 0 and C_delta <= 0  and G_delta <= 0 and T_delta <= 0 and tail < head):
            temp = head - tail
            min_sub = min(temp, min_sub)
            char_tail = string[tail]
            #print "char_tail: " + char_tail
            tail += 1
            if char_tail == 'A':
                A_delta += 1
            elif char_tail == 'C':
                C_delta += 1
            elif char_tail == 'G':
                G_delta += 1
            elif char_tail == 'T':
                T_delta += 1
    return min_sub
str_len = int(raw_input().strip())
string = raw_input().strip()
print string_replacement(string,str_len)