from seasons import get_date

import datetime
import pytest


def test_normal_date():
    assert get_date('2022-11-21') == datetime.date(2022, 11, 21)
    assert get_date('2021-11-21') == datetime.date(2021, 11, 21)

def test_wrong_format():
    with pytest.raises(SystemExit):
        get_date('2022-22-22')
    with pytest.raises(SystemExit):
        get_date('jura')
    with pytest.raises(SystemExit):
        get_date('2022=12=12')
