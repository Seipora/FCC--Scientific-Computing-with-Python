# Write a function named add_time that takes in two required parameters and one optional parameter:
# a start time in the 12-hour clock format (ending in AM or PM)
# a duration time that indicates the number of hours and minutes
# (optional) a starting day of the week, case insensitive

def add_time(start, duration, weekday=""):
    first_part = start.split(" ")
    periods = first_part[1]  # getting value "AM" or "PM"

    second_part = first_part[0].split(":")
    hour = int(second_part[0])  # Getting current hour
    minutes = int(second_part[1])  # Getting current minutes

    third_part = duration.split(":")
    added_hour = int(third_part[0])  # Getting hour that will be added
    added_minutes = int(third_part[1])  # Getting minutes that will be added

    new_minutes = minutes + added_minutes  # Adding up minutes
    new_hour = hour + added_hour  # Adding up hours

    # If minutes are > 60, it should add 1 h
    if new_minutes >= 60:
        new_minutes = new_minutes - 60
        new_hour += 1
    # All minutes need to be printed as "0n" if less than 10
    if new_minutes < 10:
        new_minutes = "0" + str(new_minutes)

    calculation = new_hour - (int(new_hour/12)*12)  # Dividing summed hours to for checking period change
    if calculation == 0:
        final_hour = 12  # in case it's midnight
    else:
        final_hour = calculation

# If the result will be the next day, it should show (next day) after the time.
# If the result will be more than one day, it should show (n days later), where "n" is the number of days later.

    days = None
    number_of_days = ""
    if new_hour >= 12:  # In either case ("PM and AM") the summ will be more than 12 if shift happens
        new_period = int(new_hour/12)
        days = round(new_hour/24)  # In case it's more days and not next day

        if periods == "AM":

            # Days change
            if new_period == 1:
                number_of_days = ""  # Same day
            elif new_period < 3:  # Two shifts (1 PM and 1 AM)
                number_of_days = "next day"
            elif days > 1:
                number_of_days = days  # More days

            # Periods change
            if new_period % 2 == 0:  # If current is AM, every even number will be AM again
                final_period = "AM"
            else:
                final_period = "PM"

        else:  # if current is PM

            # Days change
            if new_period == 1 or new_period == 2:  # first shift is immediately next day (because of PM)
                number_of_days = "next day"
            elif days > 1:
                number_of_days = days

            # Periods change
            if new_period % 2 == 0:
                final_period = "PM"
            else:
                final_period = "AM"
    else:
        final_period = periods  # No shifting (same day)

    # Day of week
    days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    future_day_print = ""  # If the result is n days later

    # Scanning for index number of given day
    for day in days_list:

        if day.upper() == weekday.upper():
            current_day = day
            index_number = days_list.index(current_day)  # Getting index of the day from the list

            if number_of_days == "next day":  # For the next day
                index_number += 1
            elif number_of_days == days:  # If it gets out of the list (looping through list multiple times)
                index_number += int(days)
                if index_number > 6:  # 6 is the last index in list
                    index_number = index_number % 7  # modulo of 7 is the index of future day in list

            future_day = days_list[index_number]  # getting value of index
            future_day_print = "," + " " + future_day

# Printing out multiple variations
    # For all variables
    new_time = "%s:%s %s%s (%s days later)" % (final_hour, new_minutes, final_period, future_day_print, number_of_days)
    # For next day, without day of the week
    new_time1 = "%s:%s %s%s (%s)" % (final_hour, new_minutes, final_period, future_day_print, number_of_days)
    # For next day, with day of the week
    new_time4 = "%s:%s %s%s (%s)" % (final_hour, new_minutes, final_period, future_day_print, number_of_days)
    # More days without day of week
    new_time2 = "%s:%s %s (%s days later)" % (final_hour, new_minutes, final_period, number_of_days)
    # For same day
    new_time3 = "%s:%s %s%s" % (final_hour, new_minutes, final_period, future_day_print)

    if number_of_days == "":
        return new_time3
    elif number_of_days == "next day":
        if len(weekday) < 1:
            return new_time1
        else:
            return new_time4
    elif weekday == "":
        return new_time2
    else:
        return new_time


