from lib.count_words import *

def test_input():
    assert count_words("words") == 1
def test_two__words():
    assert count_words("two words") == 2
def test_empty_input():
    assert count_words("") == 0