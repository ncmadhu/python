# Enter your code here. Read input from STDIN. Print output to STDOUT
string = str(raw_input().strip())

#print string
string = string.replace(" ", "").lower()
chars = set(list(string))
if len(chars) == 26:
    print "pangram"
else:
    print "not pangram"