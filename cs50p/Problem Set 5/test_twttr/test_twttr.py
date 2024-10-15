from twttr import shorten

def test_lowercase():
    assert shorten('jura') == 'jr'

def test_uppercase():
    assert shorten('JURA') == 'JR'

def test_uppercase_lowercase():
    assert shorten('AEIOUaeiou') == ''

def test_numbers():
    assert shorten('123') == '123'

def test_punctuation():
    assert shorten('...') == '...'
