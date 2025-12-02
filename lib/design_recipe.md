# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can find my tasks among all my notes
I want to check if a line from my notes includes the string `#TODO`.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def check_for_todo(str):
    """check if a line from my notes includes the string `#TODO`.

    Parameters: (list all parameters and their types)
        str: a string containing words (e.g. `#TODO`)

    Returns: ()
        Boolean: True/False

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a string contains `#TODO`
It returns True
"""
test_check_string_includes_todo():
    result = check_for_todo("#TODO buy milk and eggs")
    assert result == True

"""
Given a string does NOT contains `#TODO`
It returns False
"""
test_check_string_does_not_include_todo():
    result = check_for_todo("buy milk and eggs")
    assert result == False

"""
Given a string is empty
It returns an error message 
"""
test_check_string_is_empty():
    result = check_for_todo("")
    assert result == "String cant be empty!"

"""
Given not a string
It returns an error message 
"""
test_check_not_a_string():
    result = check_for_todo(53543)
    assert result == "Value must be a string!"


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
