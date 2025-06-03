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
        An string value of how many minutes it would take to read the text, rounded to the nearest minute.

    Side effects: (state any side effects)
        May only give time to nearest minute
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a string of less than 200 words
It returns a string indicating that it would take less than a minute
"""
estimate_time("word") => "less than 1 minute"

"""
Given a string of 200 words exactly
It returns a string indicating that it would take one minute
"""
estimate_time("word"*200) => "one minute"

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
