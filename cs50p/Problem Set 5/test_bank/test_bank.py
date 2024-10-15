from bank import value

def test_lower():
    assert value('hello') == 0
    assert value('hey') == 20

def test_upper():
    assert value('HELLO') == 0
    assert value('HEY') == 20

def test_lower_upper():
    assert value('HeLLo') == 0

def test_space():
    assert value('  hello') == 0

def test_punctuation():
    assert value('.hello') == 100

def test_number():
    assert value('123') == 100
