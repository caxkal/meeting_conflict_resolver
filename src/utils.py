from datetime import datetime, time


def convert_submission(datetime_str):
    return datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")

def convert_meeting(datetime_str):
    return datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")

def stringify_date(date_time):
    return date_time.strftime("%Y-%m-%d")

def stringify_time(date_time):
    return date_time.strftime("%H:%M")

def parse_working_hours(line):
    start_time, end_time = line.strip().split()
    valid_start_time = time(
        hour=int(start_time[:-2]), minute=int(start_time[2:]))
    valid_end_time = time(hour=int(end_time[:-2]), minute=int(end_time[2:]))

    return valid_start_time, valid_end_time
