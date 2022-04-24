def add_time(start, duration, weekday=None):
    import re

    weekdays_array = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", " Saturday", "Sunday"]
    weekdays_index = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5,
                      "sunday": 6}
    am_or_pm_flip = {"AM": "PM", "PM": "AM"}

    duration_tuple = duration.partition(":")
    duration_hours = int(duration_tuple[0])
    duration_minutes = int(duration_tuple[2])

    start_tuple = re.split(":| ", start)
    start_hours = int(start_tuple[0])
    start_minutes = int(start_tuple[1])
    am_or_pm = start_tuple[2].upper()

    end_minutes = start_minutes + duration_minutes
    end_hours = start_hours + duration_hours

    end_hours_flip = 0
    day_check = 0
    hours_flip = 0
    if end_minutes >= 60:
        end_hours_flip = int(end_minutes / 60)
        end_minutes = end_minutes % 60
        end_hours += end_hours_flip

    if end_hours >= 12:
        hours_flip = int((end_hours_flip + end_hours)/12)

    for i in range(hours_flip):
        if "AM" in am_or_pm:
            am_or_pm = am_or_pm_flip["AM"]
        else:
            am_or_pm = am_or_pm_flip["PM"]
            day_check = day_check + 1

    if "AM" in am_or_pm:
        end_hours = (end_hours % 12)
        if end_hours == 0:
            end_hours = 12
    else:
        end_hours = (end_hours % 12)
        if end_hours == 0:
            end_hours = 12

    if weekday is not None:
        week_day = str(weekday).lower()
        week_day_number = weekdays_index[week_day]
        weekday_day = (day_check + week_day_number) % 7
        week_day = weekdays_array[weekday_day]

        if day_check == 0:
            new_time = f"{str(end_hours)}:{str(end_minutes).zfill(2)} {am_or_pm}, {week_day}"
        elif day_check == 1:
            new_time = f"{str(end_hours)}:{str(end_minutes).zfill(2)} {am_or_pm}, {week_day} (next day)"
        else:
            new_time = f"{str(end_hours)}:{str(end_minutes).zfill(2)} {am_or_pm}, {week_day} ({day_check} days later)"

    else:
        if day_check == 0:
            new_time = f"{str(end_hours)}:{str(end_minutes).zfill(2)} {am_or_pm}"
        elif day_check == 1:
            new_time = f"{str(end_hours)}:{str(end_minutes).zfill(2)} {am_or_pm} (next day)"
        else:
            new_time = f"{str(end_hours)}:{str(end_minutes).zfill(2)} {am_or_pm} ({day_check} days later)"

    return new_time