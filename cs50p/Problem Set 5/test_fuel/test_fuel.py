from fuel import convert, gauge
import pytest

def test_fractions():
    assert convert('3/4') == 75
    assert convert('1/2') == 50

def test_zero_fraction():
    with pytest.raises(ZeroDivisionError):
        convert('4/0')

def test_greater_x():
    with pytest.raises(ValueError):
        convert('5/4')

def test_str():
    with pytest.raises(ValueError):
        convert('3/j')

def test_E():
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'

def test_F():
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'

def test_gauge():
    assert gauge(50) == '50%'
    assert gauge(25) == '25%'
