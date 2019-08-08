inputString = raw_input()
date, month, year = inputString.split(" ")

date = int(date)
month = int(month)
year = int(year)

if month in (1,3,5,7,8,10,12):

    if (date == 1) and (month == 1):
        prevDate = 31
        prevMonth = 12
        prevyear = year - 1
    elif (date == 1) and (month == 3):
        if (year % 4 == 0):
            prevDate = 29
        else:
            prevDate = 28
        prevMonth = 2
        prevyear = year
    elif (date == 1):
        prevDate = 30
        prevMonth = month - 1
        prevyear = year
    else:
        prevDate = date -1
        prevMonth = month
        prevyear = year

else:

    if (date == 1):
        prevDate =  31
        prevMonth = month - 1
        prevyear = year
    else:
        prevDate = date - 1
        prevMonth = month
        prevyear = year

print "%s %s %s" % (prevDate, prevMonth, prevyear)
