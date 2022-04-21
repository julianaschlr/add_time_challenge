def add_time(start, duration, week="Weekday"):
    import re

    weekdays_array = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", " Saturday", "Sunday"]
    weekdays_index = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, " saturday": 5,
                      "sunday": 6}

    duration_tuple = duration.partition(":")
    duration_hours = int(duration_tuple[0])
    duration_minutes = int(duration_tuple[1])

    start_tuple = re.split(":| ", start)
    start_hours = int(start_tuple[0])
    start_minutes = int(start_tuple[1])
    am_or_pm = start_tuple[2].upper()

    end_minutes = start_minutes + duration_minutes
    end_hours = start_hours + duration_hours

    check = False

    while check is not True:

        if end_minutes >= 60:
            end_minutes = end_minutes - 60
            end_hours += 1

        if end_hours > 12:
            end_hours = end_hours - 12
            if am_or_pm == "AM":
                am_or_pm = "PM"
            else:
                am_or_pm = "AM"

        if end_minutes > 60 or end_hours > 12:
            check = False
        else:
            check = True

        return new_time