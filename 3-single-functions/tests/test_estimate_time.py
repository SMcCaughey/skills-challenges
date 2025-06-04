from lib.estimate_time import *
import pytest as py

def test_estimate_time_with_less_than_200_words():
    result = estimate_time("word "*100)
    assert result == 0.5
def test_estimate_time_200_words():
    result = estimate_time("word "*200)
    assert result == 1.0
def test_estimate_time_376_words():
    result = estimate_time("word "*376)
    assert result == 1.88
def test_estimate_no_input():
    with py.raises(Exception) as e:
        estimate_time("")
    error_message = str(e.value)
    assert error_message == "You can't read what is not there."