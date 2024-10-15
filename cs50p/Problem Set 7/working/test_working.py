from working import convert

import pytest

def test_hours():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('1 PM to 3 PM') == '13:00 to 15:00'

def test_minutes():
    assert convert('9:25 AM to 5:35 PM') == '09:25 to 17:35'
    assert convert('1:00 PM to 3:55 PM') == '13:00 to 15:55'

def test_error():
    with pytest.raises(ValueError):
        convert('13 AM to 5 PM')
    with pytest.raises(ValueError):
        convert('1:60 PM to 3:55 PM')

def test_wrong_input():
    with pytest.raises(ValueError):
        convert('12 AM - 5 PM')
    with pytest.raises(ValueError):
        convert('1:50 PM - 3:55 PM')
