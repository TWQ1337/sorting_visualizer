from typing import Any


def merge_sort_check_input(list_of_values: list[Any]) -> list[int]:
    # Helper Function that checks for non integers to raise Typeerror
    for index_value, item in enumerate(list_of_values):
        if not isinstance(item, int):
            raise TypeError(f'The element of list at index {index_value} is not an integer, {item}')
    return list_of_values


def merge_sort_execute(numbers_list: list[int]) -> list[int]:
    """
    Recurve function that splits the list
    """
    # Base case scenario for the recursive function
    if len(numbers_list) == 1:
        return numbers_list
    # Splitting the list into two by slicing it in the middle
    mid_list_index: int = len(numbers_list) // 2
    left_list: list[int] = numbers_list[:mid_list_index]
    right_list: list[int] = numbers_list[mid_list_index:]

    return merge_lists(merge_sort_execute(left_list), merge_sort_execute(right_list))


def merge_lists(left: list[int], right: list[int]) -> list[int]:
    """
    Showcase of typeerror, excessive in this situation.
    for index_value, item in enumerate(left):
        if not isinstance(item, int):
            raise TypeError(f'The element of "left" list at index {index_value} is not an integer')
    for index_value, item in enumerate(right):
        if not isinstance(item, int):
            raise TypeError(f'The element of "right" list at index {index_value} is not an integer')
    """

    # Setting the starting helper values
    combined_list: list[int] = []
    left_index: int = 0
    right_index: int = 0

    """
    Iterating trough both lists until we have no values left in one of them
    Comparing the values and adding the smallest one to the end of the combined list
    """
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            combined_list.append(left[left_index])
            left_index += 1
        else:
            combined_list.append(right[right_index])
            right_index += 1

    # Adding the rest of the list
    while left_index < len(left):
        combined_list.append(left[left_index])
        left_index += 1
    while right_index < len(right):
        combined_list.append(right[right_index])
        right_index += 1

    return combined_list


def merge_sort(numbers_list: list[int]) -> list[int]:
    # Main Function for Merge sort that checks the list and sorts it
    return merge_sort_execute(merge_sort_check_input(numbers_list))
