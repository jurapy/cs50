from um import count

def test_ignorecase():
    assert count('Um') == 1
    assert count('um') == 1

def test_sentence():
    assert count('um its fine') == 1
    assert count('um its extra um fine') == 2

def test_punctuation_after_um():
    assert count('um,') == 1
    assert count('um.') == 1
    assert count('um?') == 1
    assert count('um!') == 1

def test_um_inside_word():
    assert count('yummi') == 0
    assert count('today is bummer') == 0
