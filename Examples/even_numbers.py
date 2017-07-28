# Author: Madhu Chakravarthy
# Date: 28-07-2017

def even_num_count(num_string, count_at_index, index):

    if index == len(num_string):
        return 0 
    else:
        if int(num_string[index]) % 2 == 0:
            count = 1 + even_num_count(num_string,count_at_index,index + 1)
        else:
            count = even_num_count(num_string,count_at_index,index + 1)
        count_at_index.insert(0,str(count))
        return count

def even_count(num_string, count_at_index, index):

    str_length = len(num_string)

    for i in range(str_length, index - 1, -1):
        if i == str_length:
            count_so_far = 0
        else:
            if int(num_string[i]) % 2 == 0:
                count_so_far = 1 + count_so_far
            count_at_index.insert(0,str(count_so_far))



if __name__ == "__main__":

    count_at_index = [] 
    num_string = "574674546476"
    #even_num_count(num_string,count_at_index,0)
    even_count(num_string,count_at_index,0)
    print " ".join(count_at_index)







