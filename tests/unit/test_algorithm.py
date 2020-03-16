import src.algorithm
from src.meeting_slot import MeetingSlot
from datetime import datetime, time

def set_basic_meetings():
    slot1 = MeetingSlot(user_id="user_id1", submittion_time=datetime.now(), 
        start_meeting=datetime(2020, 3, 2, 10, 00), end_meeting=datetime(2020, 3, 2, 12, 00))

    slot2 = MeetingSlot(user_id="user_id2", submittion_time=datetime.now(), 
        start_meeting=datetime(2020, 3, 2, 11, 00), end_meeting=datetime(2020, 3, 2, 13, 00))
    meetings = {"date": [slot1, slot2]}
    return meetings

def test_core_algorithm_conflict():
    ("check algorithm with two conflicting meetings")

    conflict_meetings = set_basic_meetings()
    results = src.algorithm.run(conflict_meetings)
    for el in results.values():
        el.should.have.length_of(1)
        el[0].user_id.should.be("user_id1")

def test_core_algorithm_conflict_with_changed_submit_time():
    ("check algorithm with two conflicting meetings with revered submit time")

    conflict_meetings = set_basic_meetings()
    # update meeting submittion time
    conflict_meetings["date"][0].submittion_time = datetime.now()
    results = src.algorithm.run(conflict_meetings)
    
    # Check that result is not empty
    results.shouldnt.be.empty
    for el in results.values():
        
        # check that there only one meeting
        el.should.have.length_of(1)

        # And the meeting for specific user was approved
        el[0].user_id.should.be("user_id2")

def test_core_algorithm_no_conflict():
    ("check algorithm with two normal meetings")

    meetings = set_basic_meetings()
    # change conflicting meeting
    meetings["date"][-1].start_meeting = datetime(2020, 3, 2, 12, 00)
    results = src.algorithm.run(meetings)

    # Check that result is not empty
    results.shouldnt.be.empty
    for el in results.values():
        
        # check that there are two meetings every day
        el.should.have.length_of(2)

def test_core_algorithm_many_days():
    ("check algorithm with many days")

    meetings = set_basic_meetings()
    
    # Add the same meetings for new date
    meetings["date2"] = meetings["date"]

    results = src.algorithm.run(meetings)

    results.keys().should.have.length_of(2)
    for el in results.values():
        el.should.have.length_of(1)
        el[0].user_id.should.be("user_id1")


