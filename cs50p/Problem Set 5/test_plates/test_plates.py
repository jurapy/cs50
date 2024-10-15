from plates import is_valid

def test_lenghts():
    assert is_valid('') == False
    assert is_valid('A') == False
    assert is_valid('1234567') == False

def test_start_2letters():
    assert is_valid('AA') == True
    assert is_valid('A2') == False

def test_letters():
    assert is_valid('AA') == True

def test_letters_with_numbers():
    assert is_valid('AA123') == True

def test_punctuation():
    assert is_valid('...') == False

def test_letters_after_numbers():
    assert is_valid('AA123AA') == False

def test_numbers_in_middle():
    assert is_valid('AA12A1') == False

def test_first_number_zero():
    assert is_valid('AA012') == False

def test_isalphanumeric():
    assert is_valid('AA1.!?') == False
