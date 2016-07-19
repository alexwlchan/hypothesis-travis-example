from datetime import date
from hypothesis import given
from hypothesis.extra.datetime import dates as date_strategy


def next_birthday(birthday):
    """Returns somebody's next birthday after today."""
    current_year = date.today().year
    month, day = birthday.month, birthday.day

    birthday = date(current_year, month, day)
    if birthday < date.today():
        birthday = date(current_year + 1, month, day)

    return birthday


@given(date_strategy(min_year=1850, max_year=2015))
def test_next_birthday_is_after_today(birthday):
    assert date.today() <= next_birthday(birthday)