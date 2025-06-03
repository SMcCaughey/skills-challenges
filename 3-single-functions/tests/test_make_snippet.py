from lib.make_snippet import *

def test_input():
    assert snippet("word") == "word"
def test_two_words():
    assert snippet("two words") == "two words"
def test_six_words():
    assert snippet("there are six words in this") == "there are six words in" + "..."
def test_no_words():
    assert snippet("") == ""
def test_punctuation_less_than_five_words():
    assert snippet("synonymous/similar") == "synonymous/similar"
def test_punctuation_more_than_five_words():
    assert snippet("synonymous/similar/close/related/equivalent/same") == "synonymous/similar/close/related/equivalent" + "..."