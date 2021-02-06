import sys
# insert at position 1 in the path, as 0 is the path of this file.

sys.path.insert(0, '../src')
from range import Range 
import pytest

class TestRange:

    @pytest.mark.parametrize("Range, num, expected_result", [
        (Range(19), 1, True),
        (Range(2, 10), 9, True),
        (Range(34, 293), 100, True),
        (Range(9), 11, False),
        (Range(-123, -12), 1231, False),
    ])
    def test_contains(self, Range, num, expected_result):
        assert Range.contains(num) == expected_result

    @pytest.mark.parametrize("Range, obj, expected_result", [
        (Range(19), Range(17, 21), False),
        (Range(2, 10), Range(4), True),
        (Range(34, -93), Range(-110, 0), True),
        (Range(9), Range(6, 8), False),
        (Range(-123, -12), Range(-10, 0), False),
    ])
    def test_left_overlap(self, Range, obj, expected_result):
         assert Range.left_overlap(obj) == expected_result

    @pytest.mark.parametrize("Range, obj, expected_result", [
        (Range(19), Range(17, 21), True),
        (Range(2, 10), Range(4), False),
        (Range(34, -93), Range(-110, 0), False),
        (Range(9), Range(6, 8), False),
        (Range(-123, -12), Range(-10, 0), False),
    ])
    def test_right_overlap(self, Range, obj, expected_result):
         assert Range.right_overlap(obj) == expected_result     

    @pytest.mark.parametrize("Range, obj, expected_result", [
        (Range(19), Range(0, 19), True),
        (Range(2, 10), Range(2, 10), True),
        (Range(34, -93), Range(-93, 34), True),
        (Range(9), Range(6, 8), False),
        (Range(10), Range(-10, 0), False),
    ])
    def test_is_same(self, Range, obj, expected_result):
         assert Range.is_same(obj) == expected_result

    @pytest.mark.parametrize("Range, obj, expected_result", [
        (Range(19), Range(17, 21), (0, 21)),
        (Range(2, 10), Range(4), (0, 10)),
        (Range(34, -93), Range(-110, 0), (-110, 34)),
        (Range(9), Range(6, 8), (0, 9)),
        (Range(-123, -12), Range(-10, 0), (-123, 0)),
    ])
    def test_merge(self, Range, obj, expected_result):
        merge_obj = Range.merge(obj) 
        assert (merge_obj.low, merge_obj.high)  == expected_result



    @pytest.mark.parametrize("Range, obj, expected_result", [
        (Range(19, 21), Range(21, 54), True),
        (Range(2, 10), Range(4), False),
        (Range(34, 1), Range(-110, 0), False),
        (Range(6), Range(6, 8), True),
        (Range(1, -12), Range(-10, 0), False),
    ])
    def test_is_touching(self, Range, obj, expected_result):
         assert Range.is_touching(obj) == expected_result

    @pytest.mark.parametrize("Range, obj, expected_result", [
        (Range(19), Range(20, 87), True),
        (Range(2, 10), Range(2), False),
        (Range(34, -93), Range(-110, -94), True),
        (Range(9), Range(6, 8), False),
        (Range(-23, -12), Range(23, 12), True),
    ])
    def test_is_disjoint(self, Range, obj, expected_result):
         assert Range.is_disjoint(obj) == expected_result
    
    @pytest.mark.parametrize("Range, extend_by , expected_result", [
        (Range(1, 10), 2, -1),
        (Range(-23, -90), 12, -102),
        (Range(-23, -90), -12, -23),
        (Range(-23, -90), -12, -23),
    ])  
    def test_lstretch(self, Range, extend_by, expected_result):
        if extend_by < 0:
            with pytest.raises(ValueError):
                Range.l_stretch(extend_by)
                assert Range.low == expected_result
        else:
            Range.l_stretch(extend_by)
            assert Range.low == expected_result   
    
    @pytest.mark.parametrize("Range, extend_by , expected_result", [
        (Range(1, 10), 2, 12),
        (Range(-23, -90), 12, -11),
        (Range(-23, -90), -12, -23),
    ])  
    def test_rstretch(self, Range, extend_by, expected_result):
        if extend_by < 0:
            with pytest.raises(ValueError):
                Range.r_stretch(extend_by)
                assert Range.high == expected_result
        else:
            Range.r_stretch(extend_by)
            assert Range.high == expected_result
    
    @pytest.mark.parametrize("Range, extend_by , expected_result", [
        (Range(1, 10), 2, (-1, 12)),
        (Range(-23, -90), 12, (-102, -11)),
        (Range(4, -45), 10, (14, -55)),
        (Range(-23, -90), -12, (-23, -90)),
    ])  

    def test_stretch(self, Range, extend_by, expected_result):
        if extend_by < 0:
            with pytest.raises(ValueError):
                Range.stretch(extend_by)
                assert (Range.low, Range.high) == (min(expected_result), max(expected_result))

        else:
            Range.stretch(extend_by)
            assert (Range.low, Range.high) ==  (min(expected_result), max(expected_result))
 

    @pytest.mark.parametrize("Range, shift_by , expected_result", [
        (Range(1, 10), 2, (3, 12)),
        (Range(-23, -90), 12, (-78, -11)),
        (Range(4, -45), 10, (14, -35)),
        (Range(-23, -90), -12, (-35, -102)),
    ])  

    def test_shift(self, Range, shift_by, expected_result):
        Range.shift(shift_by)
        assert (Range.low, Range.high) ==  (min(expected_result), max(expected_result))                  