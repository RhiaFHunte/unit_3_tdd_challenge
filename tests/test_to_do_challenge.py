import pytest 
from lib.to_do_challenge import *


def test_check_string_includes_todo():
    result = check_for_todo("#TODO buy milk and eggs")
    assert result == True

def test_check_string_does_not_include_todo():
    result = check_for_todo("buy milk and eggs")
    assert result == False

def test_check_string_is_empty():
    with pytest.raises(Exception) as e:
        check_for_todo("")
    error_message = str(e.value)
    assert error_message == "String cant be empty!"

def test_check_not_a_string():
    with pytest.raises(Exception) as e:
        check_for_todo(53543)
    error_message = str(e.value)
    assert error_message == "Value must be a string!"

