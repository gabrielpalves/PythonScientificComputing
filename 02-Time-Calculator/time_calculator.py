def add_time(start, duration, weekday=""):

    weekdays = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")

    pos = start.find(":")
    space = start.find(" ")

    h = int(start[0:pos])
    if "p" in start.lower(): # it seems that the user has to type correctly, so it is either AM or PM
        h = h + 12 # if it is PM, add 12 hours. Later it will return to the initial format

    m = int(start[pos+1:space])

    pos = duration.find(":")
    hd = int(duration[0:pos])
    md = int(duration[pos+1:])

    newm = m + md
    rest = 0
    if newm > 60:
        nm = newm%60
        rest = (newm-nm)/60
        newm = nm
        
    newh = h + hd + rest

    minutes = newm/60 # minutes as 0.xx hours
    total = newh+minutes
    strdays = ""
    daysPassed = 0
    if total > 24: # it passed at least one day
        daysPassed = (total/24)
        daysPassed = daysPassed - daysPassed%1
        if daysPassed == 1:
            strdays = " (next day)"
        else:
            strdays = " (" + str(int(daysPassed)) + " days later)"
    
    # get the correct weekday, if informed by user
    if weekday:
        for iter, item in enumerate(weekdays):
            if weekday.lower() == item:
                wd = iter
        wd = (wd + daysPassed)%7
        strdays = " " + weekdays[int(wd)].title() + strdays

    newh = newh%24
    
    if newh >= 12:
        if newh != 12:
            newh = newh-12

        if strdays != "":
            if weekday:
                strdays = " PM," + strdays
            else:
                strdays = " PM" + strdays
        else:
            strdays = " PM"
    else:
        if newh == 0:
            newh = 12

        if strdays != "":
            if weekday:
                strdays = " AM," + strdays
            else:
                strdays = " AM" + strdays
        else:
            strdays = " AM"
    
    newm = int(newm)
    newh = int(newh)
    if newm < 10:
        newm = "0" + str(newm)
    else:
        newm = str(newm)
    new_time = str(newh) + ":" + newm + strdays

    return new_time