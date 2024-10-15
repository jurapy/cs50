from jar import Jar
import pytest

def test_init():
    jar = Jar(12)
    assert jar.capacity == 12

def test_str():
    jar = Jar(12)
    jar.deposit(3)
    assert str(jar) == '🍪🍪🍪'

def test_deposit():
    jar = Jar(11)
    jar.deposit(10)
    assert jar.size == 10
    with pytest.raises(ValueError):
        jar.deposit(2)

def test_withdraw():
    jar = Jar(11)
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.withdraw(3)
