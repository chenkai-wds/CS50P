from datetime import date
from seasons import get_total_minutes


def test_get_minutes():
    assert get_total_minutes(date(1999, 1, 1), date(2024, 7, 28)) == 13449600
    assert get_total_minutes(date(1999, 12, 31), date(2024, 7, 28)) == 12925440
    assert get_total_minutes(date(1970, 1, 1), date(2024, 7, 28)) == 28702080
