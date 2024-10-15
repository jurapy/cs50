from numb3rs import validate

def test_real_ip():
    assert validate('0.0.0.0') == True
    assert validate('192.168.1.1') == True
    assert validate('255.255.255.255') == True

def test_wrong_ip():
    assert validate('1.1.1.1.1') == False
    assert validate('256.256.256.256') == False
    assert validate('255.255.255.256') == False

def test_str():
    assert validate('cat') == False

def test_punctuation():
    assert validate('?._!') == False
