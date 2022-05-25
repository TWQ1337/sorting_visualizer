from typing import Any
import pytest
from various_sort_visualization.merge_sort import merge_lists, merge_sort_execute, merge_sort_check_input, merge_sort


def test_merge_sort_whole_functionality():
    # Testing the combined function merge sort on valid input and comparing it to inbuilt sort result
    list_of_unsorted_numbers: list[int] = [20, 1, 5, 6, 2, 3, 4, 45, 24, 7]
    returned_sorted_list = merge_sort(list_of_unsorted_numbers)
    list_of_unsorted_numbers.sort()
    assert returned_sorted_list == list_of_unsorted_numbers


def test_merge_sort_execute_base_functionality():
    # Test compares sorting result of inbuilt sort function and merge_sort_execute
    list_of_unsorted_numbers: list[int] = [20, 1, 5, 6, 2, 3, 4, 45, 24, 7]
    sorted_list: list[int] = merge_sort_execute(list_of_unsorted_numbers)
    list_of_unsorted_numbers.sort()
    assert sorted_list == list_of_unsorted_numbers


def test_merge_lists_basic_sort():
    # Sequence of positive numbers in two presorted lists for testing basic funcionality
    positive_merge_left: list[int] = [2, 5, 6, 7, 8]
    positive_merge_right: list[int] = [1, 3, 4, 9]
    combined_list = merge_lists(positive_merge_left, positive_merge_right)
    # Comparing sorting with inbuilt function as a reference
    test_array: list[int] = positive_merge_left + positive_merge_right
    test_array.sort()
    assert combined_list == test_array


def test_merge_sort_check_input_basic():
    # Checking that input and output of the function is the same with the correct input
    list_of_unsorted_numbers: list[int] = [20, 1, 5, 6, 2, 3, 4, 45, 24, 7]
    returned_list_of_unsorted_numbers = merge_sort_check_input(list_of_unsorted_numbers)
    assert returned_list_of_unsorted_numbers == list_of_unsorted_numbers


def test_merge_sort_check_input_error():
    # Test for expected error of non integer inputs; index 3 'dog'
    list_of_wrong_inputs: list[Any] = [20, 1, 5, 'dog', 2, 3, 4, 45, 'cat', 7]
    with pytest.raises(TypeError):
        merge_sort_check_input(list_of_wrong_inputs)


@pytest.mark.skip(reason='functionality removed')
def test_merge_lists_type_error_input():
    # Test for commented out functionality on merge_list function, see test_merge_sort_check_input_error
    # Presorted lists with left list having a wrong type element
    positive_merge_left: list[int] = [2, 'five', 6, 7, 8]
    positive_merge_right: list[int] = [1, 3, 4, 9]

    with pytest.raises(TypeError):
        merge_lists(positive_merge_left, positive_merge_right)
