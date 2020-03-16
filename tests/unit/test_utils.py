import src.utils
from datetime import datetime, time

def test_convert_submission():
    ("check convert submission")
    
    b = datetime(2017, 11, 28, 23, 55, 59)
    date = "2017-11-28 23:55:59"
    src.utils.convert_submission(date).should.be.equal(b)

def test_convert_meeting():
    ("check convert meeting")
    
    b = datetime(2020, 3, 2, 20, 12)
    date = "2020-03-02 20:12"
    src.utils.convert_meeting(date).should.be.equal(b)

def test_stringify_date():
    ("check stringify date")
    
    date = datetime(2020, 3, 2, 20, 12)
    date_str = "2020-03-02"
    src.utils.stringify_date(date).should.be.equal(date_str)


def test_stringify_time():
    ("check stringify time")
    
    date = datetime(2020, 3, 2, 20, 12)
    time_str = "20:12"
    src.utils.stringify_time(date).should.be.equal(time_str)

def test_parse_working_hours():
    ("check parse working hours")
    
    input_line = '1000 1935'
    start_time = time(10, 00)
    end_time = time(19, 35)
    src.utils.parse_working_hours(input_line).should.be.equal((start_time, end_time))

