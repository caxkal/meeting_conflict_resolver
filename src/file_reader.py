
from datetime import timedelta, time

from src.meeting_slot import MeetingSlot
from src.utils import parse_working_hours, convert_submission, convert_meeting, stringify_date, stringify_time


def parse_first_line(line):
    first_line = line.strip().split()
    dt = " ".join(first_line[:-1])
    user_id = first_line[-1]
    submittion_time = convert_submission(dt)
    return user_id, submittion_time


def parse_second_line(line):
    second_line = line.strip().split()
    dt = " ".join(second_line[:-1])
    duration = second_line[-1]
    start_meeting = convert_meeting(dt)
    end_meeting = start_meeting + timedelta(hours=int(duration))
    return start_meeting, end_meeting


def parse_file(filename):
    meetings = {}
    with open(filename) as f:
        initial_line = f.readline()
        # get working hours from file
        valid_start_time, valid_end_time = parse_working_hours(initial_line)
        while True:
            first_line = f.readline()
            second_line = f.readline()

            if not second_line:
                break

            user_id, submittion_time = parse_first_line(first_line)
            start_meeting, end_meeting = parse_second_line(second_line)
            slot = MeetingSlot(user_id, submittion_time,
                               start_meeting, end_meeting)
            
            # Collect all valid meeting requests grouped by date
            if slot.is_valid(valid_start_time, valid_end_time):
                date = stringify_date(slot.start_meeting)
                if date in meetings.keys():
                    meetings[date].append(slot)
                else:
                    meetings[date] = [slot]

    return meetings
