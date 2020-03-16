from src.meeting_slot import MeetingSlot
from datetime import datetime, time

def test_meeting_slot_class_constructor():
    ("check constructor")

    user_id = "123"
    submittion_time = "XYZ"
    start_meeting = "start"
    end_meeting = "end"

    # Create object of MeetingSlot
    slot = MeetingSlot(user_id, submittion_time, start_meeting, end_meeting)
    
    # Check that all properties exist and match with values
    slot.should.have.property("user_id").which.should.be.equal(user_id)
    slot.should.have.property("submittion_time").which.should.be.equal(submittion_time)
    slot.should.have.property("start_meeting").which.should.be.equal(start_meeting)
    slot.should.have.property("end_meeting").which.should.be.equal(end_meeting)

def test_is_valid_meeting_slot():
    ("check validity of meeting slot")

    user_id = "123"
    submittion_time = "XYZ"
    valid_start_meeting = datetime(2020, 3, 2,10, 00)
    valid_end_meeting = datetime(2020, 3, 2, 18, 00)
    slot = MeetingSlot(user_id, submittion_time, valid_start_meeting, valid_end_meeting)

    start_time = time(10, 00)
    end_time = time(19, 35)
    slot.is_valid(start_time, end_time).should.be.true

    valid_start_meeting = datetime(2020, 3, 2, 10, 00)
    invalid_end_meeting = datetime(2020, 3, 2, 20, 00)
    slot = MeetingSlot(user_id, submittion_time, valid_start_meeting, invalid_end_meeting)
    slot.is_valid(start_time, end_time).should.be.false

    invalid_start_meeting = datetime(2020, 3, 2,9, 00)
    valid_end_meeting = datetime(2020, 3, 2,15, 00)
    slot = MeetingSlot(user_id, submittion_time, valid_start_meeting, invalid_end_meeting)
    slot.is_valid(start_time, end_time).should.be.false

    invalid_start_meeting = datetime(2020, 3, 2,9, 00)
    invalid_end_meeting = datetime(2020, 3, 2,22, 00)
    slot = MeetingSlot(user_id, submittion_time, valid_start_meeting, invalid_end_meeting)
    slot.is_valid(start_time, end_time).should.be.false

