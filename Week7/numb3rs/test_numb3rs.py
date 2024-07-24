from numb3rs import validate

def test_validData():
    assert validate("1.2.3.4") == True
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("121.78.68.21") == True

def test_invalidData():
    assert validate("1.2.3") == False
    assert validate("1.2.3.256") == False
    assert validate("1.2.3.4.5.6") == False
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False

def test_NotIntegers():
    assert validate("1.2.3.a") == False
    assert validate("cat") == False
    assert validate("a.b.c.d") == False
    assert validate("abc.abc.abc.abc") == False