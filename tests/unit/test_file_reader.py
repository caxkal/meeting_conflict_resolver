import src.file_reader
from datetime import datetime

def test_parse_first_line():
    ("check parse first line")
    
    input_line = "2011-03-15 14:19:12 EMP005"
    d = datetime(2011, 3, 15, 14,19, 12)

    src.file_reader.parse_first_line(input_line).should.be.equal(("EMP005", d))

def test_parse_second_line():
    ("check parse second line")
    
    input_line = "2011-03-27 09:00 8"
    start = datetime(2011, 3, 27, 9, 00)
    end = datetime(2011, 3, 27, 17, 00)
    src.file_reader.parse_second_line(input_line).should.be.equal((start, end))
