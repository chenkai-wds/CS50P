from twttr import shorten

def test_lower():
    assert shorten("hello") == "hll"
    assert shorten("twitter") == "twttr"
    assert shorten("aeiou") == ""

def test_upper():
    assert shorten("HELLO") == "HLL"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("AEIOU") == ""

def test_number():
    assert shorten("1234567890") == "1234567890"

def test_punctuation():
    assert shorten("What's your name?") == "Wht's yr nm?"
