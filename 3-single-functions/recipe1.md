# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def estimate_time(text):
    """Estimates how long it would take to read the text if you read it at 200 words per minute

    Parameters: (list all parameters and their types)
        text: a string containing words (e.g. "Hello World")

    Returns: (state the return value and its type)
        An float value of how many minutes it would take to read the text, with the values after the decimal being fractions of one minute rather than seconds.

    Side effects: (state any side effects)
        Will throw error if no text input.
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a string of less than 200 words
It returns a float indicating what fraction of a minute it would take to read, e.g. 0.5 = half a minute = 30 seconds.
"""
estimate_time("word "*100) => 0.5

"""
Given a string of 200 words exactly
It returns a float of 1.0
"""
estimate_time("word "*200) => 1.0

"""
Given a string of 376 words
It returns a float of 1.88
"""
estimate_time("word "*376) => 1.88

"""
Given an empty input
It throws an error saying "You can't read what is not there."
"""
estimate_time("") => "You can't read what is not there."


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.estimate_time import *

"""
Given a string of 100 words
It returns a float of 0.5
"""
def test_estimate_time_with_less_than_200_words():
    result = estimate_time("word"*100)
    assert result == 0.5

"""
Given a string of 200 words exactly
It returns a float of 1.0
"""
def test_estimate_time_200_words():
    result = estimate_time("word "*200)
    assert result == 1.0

"""
Given a string of 376 words
It returns a float of 1.88
"""
def test_estimate_time_376_words():
    result = estimate_time("word "*376)
    assert result == 1.88

"""
Given an empty input
It throws an error saying "You can't read what is not there."
"""
def test_estimate_no_input():
    import pytest as py
    with py.raises(Exception) as e:
        estimate_time("")
    error_message = str(e.value)
    assert error_message == "You can't read what is not there."
```