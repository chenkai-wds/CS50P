from plates import is_valid

def test_startsWithLetter():
    assert is_valid("A123") == False
    assert is_valid("123A") == False
    assert is_valid("AA12") == True

def test_length():
    assert is_valid("AA2345") == True
    assert is_valid("A") == False
    assert is_valid("AA123456789") == False

def test_numInMid():
    assert is_valid("AAA22A") == False
    assert is_valid("AAA222") == True
    assert is_valid("CS50P") == False

def test_firstNumNotZero():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True

def test_noFunctuatiion():
    assert is_valid("PI3.14") == False
    assert is_valid("CSP12_5") == False

def test_haveLettersAndNumber():
    assert is_valid("CS50") == True
    assert is_valid("OUTATIME") == False