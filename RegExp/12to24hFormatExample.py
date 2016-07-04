import re
pattern = re.compile("^([0-9]{2}):([0-9]{2}):([0-9]{2})(AM|PM)$")
match = pattern.findall("07:05:45PM")
print match
hour = ""
if match:
    if match[0][3] == "AM":
        if int(match[0][0]) == 12:
            hour = "00"
        else:
            hour = match[0][0]
    else:
        if int(match[0][0]) == 12:
            hour = match[0][0]
        else:
            hour = str(int(match[0][0]) + 12)
print hour + ":" + match[0][1] + ":" + match[0][2]
        
