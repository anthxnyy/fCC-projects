def add_time(start, duration, day=None):

    # Initialize variables

    start = start.split()
    start_time = start[0].split(":")
    duration_time = duration.split(":")

    start_hour, start_minute, meridiem = (
        int(start_time[0]),
        int(start_time[1]),
        start[1],
    )
    duration_hour, duration_minute = int(duration_time[0]), int(
        duration_time[1]
    )
    new_hour, new_minute = int, int
    day_increase = 0
    week_count = 0

    # Add minutes

    new_minute = start_minute + duration_minute
    while new_minute >= 60:
        new_minute -= 60
        duration_hour += 1

    # Add hours

    new_hour = start_hour + duration_hour
    while new_hour > 24:
        new_hour -= 24
        day_increase += 1
    if new_hour >= 12:
        new_hour -= 12
        if meridiem == "AM":
            meridiem = "PM"
        else:
            meridiem = "AM"
            day_increase += 1
    if new_hour == 0:
        new_hour = 12

    # Get new day

    if day is not None:
        new_day = str
        days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        day = day.lower()
        day = day.capitalize()
        day = days.index(day)
        while day_increase > 7:
            day_increase -= 7
            week_count += 1
        if (day + day_increase) > 6:
            new_day = days[day + day_increase - 7]
        else:
            new_day = days[day + day_increase]

    # Return result

    if day is not None:
        if day_increase == 1:
            return (
                f"{new_hour}:{new_minute:02d} {meridiem}, {new_day} (next day)"
            )
        elif day_increase > 1:
            return f"{new_hour}:{new_minute:02d} {meridiem}, {new_day} ({day_increase + (week_count * 7)} days later)"
        else:
            return f"{new_hour}:{new_minute:02d} {meridiem}, {new_day}"
    else:
        if day_increase == 1:
            return f"{new_hour}:{new_minute:02d} {meridiem} (next day)"
        elif day_increase > 1:
            return f"{new_hour}:{new_minute:02d} {meridiem} ({day_increase + (week_count * 7)} days later)"
        else:
            return f"{new_hour}:{new_minute:02d} {meridiem}"
