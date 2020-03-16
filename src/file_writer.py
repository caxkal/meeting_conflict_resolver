
from src.utils import stringify_date, stringify_time

def write_daily_meetings(result_slots, filename):
    with open(filename, 'w') as f:
        for daily_plan in result_slots.values():
            print(stringify_date(daily_plan[0].start_meeting), file=f)
            for slot in daily_plan:
                print("{} {} {}".format(stringify_time(slot.start_meeting), 
                    stringify_time(slot.end_meeting), slot.user_id), file=f)
