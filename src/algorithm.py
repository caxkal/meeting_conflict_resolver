
from src.file_reader import parse_file
from src.file_writer import write_daily_meetings


def run(meetings):

    result_slots = {}
    
    # iterate through all meeting buckets orderd by meeting date
    for day, value in sorted(meetings.items()):
        # sort per submittion time
        ordered_slots = sorted(value, key=lambda a: a.submittion_time)

        # put first slot into result list
        approved_slots = [ordered_slots[0]]
        for slot in ordered_slots:
            is_conflict = False
            # check if current slot has any conflict with previous ones
            for result_slot in approved_slots:
                if not (result_slot.start_meeting >= slot.end_meeting or result_slot.end_meeting <= slot.start_meeting):
                    is_conflict = True
                    break
            # in case there is no conflict add into approved meeting list
            if not is_conflict:
                approved_slots.append(slot)

        # sort by start time
        result_slots[day] = sorted(approved_slots, key=lambda a: a.start_meeting)
    return result_slots