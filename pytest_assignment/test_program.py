import pytest
from program import divide_numbers, reverse_string, get_list_element

#test that divide numbers works, should round to 2 decimal places
def test_divide_numbers():
    assert divide_numbers(10, 3) == 3.33

def test_divide_by_zero():
    assert divide_numbers(10, 0) == "Division by zero is not allowed. Please enter a non-zero number."


def test_reverse_string():
    assert reverse_string("Hello12#") == "#21OLLEh"

def test_reverse_string_int():
    assert reverse_string(123) == "321"



