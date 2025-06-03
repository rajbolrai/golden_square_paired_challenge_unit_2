from lib.high_value import *

"""
Try to make an object with the class, if not found
then should return an error
"""
def test_giving_a_high_second_value_output_second_value():
    obj_high_value = HighValue(0,1)
    result = obj_high_value.get_highest()
    assert result == "Second value is higher"

def test_giving_a_high_first_value_output_first_value():
    obj_high_value = HighValue(1,0)
    result = obj_high_value.get_highest()
    assert result == "First value is higher"

def test_giving_same_value_output_same_value():
    obj_high_value = HighValue(1,1)
    result = obj_high_value.get_highest()
    assert result == "Values are equal"

def test_invalid_first_selection_output_nothing():
    obj_high_value = HighValue(1,1)
    original_value = obj_high_value.value_first
    obj_high_value.add(1, " ")
    equal = original_value == obj_high_value.value_first
    assert equal == True

def test_invalid_second_selection_output_nothing():
    obj_high_value = HighValue(1,1)
    original_value = obj_high_value.value_second
    obj_high_value.add(1, " ")
    equal = original_value == obj_high_value.value_second
    assert equal == True

def test_valid_first_selection_output_increased_first_value():
    obj_high_value = HighValue(1,1)
    original_value = obj_high_value.value_first
    obj_high_value.add(5,"first")
    equal = original_value != obj_high_value.value_first
    assert equal == True

def test_valid_second_selection_output_increased_second_value():
    obj_high_value = HighValue(1,1)
    original_value = obj_high_value.value_second
    obj_high_value.add(5,"second")
    equal = original_value != obj_high_value.value_second
    assert equal == True