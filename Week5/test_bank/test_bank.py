from bank import value

def test_startWithHello():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("Hello, World!") == 0

def test_startWithH():
    assert value("h") == 20
    assert value("H") == 20
    assert value("Hey") == 20
    assert value("How you doing?") == 20

def test_other():
    assert value("What's up?") == 100
    assert value("What's happening") == 100