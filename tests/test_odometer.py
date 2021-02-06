import pytest
import sys
# insert at position 1 in the path, as 0 is the path of this file.
sys.path.insert(1, '../src')
from Odometer import Odometer
cd 
class Testodometer:
    
    @pytest.mark.parametrize("odometer, num, expected_result", [
        (Odometer(1), 1, True),
        (Odometer(2), 19, True),
        (Odometer(2), 90, False),
        (Odometer(2), 11, False),
        (Odometer(4), 1231, False),
    ])
    def test_is_ascending(self, odometer, num, expected_result):
        assert odometer.is_ascending(num) == expected_result

    @pytest.mark.parametrize("odometer, curr_reading, next_read", [
        (Odometer(1), 1, 2),
        (Odometer(2), 19, 23),
        (Odometer(3), 789, 123),
        (Odometer(4), 1234, 1235),
        (Odometer(5), 12356, 12357),
    ])
    def test_is_next_reading(self, odometer, curr_reading, next_read):
        assert odometer.next_reading(curr_reading) == next_read
    
    @pytest.mark.parametrize("odometer, curr_reading, prev_read", [
        (Odometer(1), 2, 1),
        (Odometer(2), 23, 19),
        (Odometer(3), 123, 789),
        (Odometer(4), 1235, 1234),
        (Odometer(5), 13679, 13678),
    ])
    def test_is_prev_reading(self, odometer, curr_reading, prev_read):
        assert odometer.previous_reading(curr_reading) == prev_read
