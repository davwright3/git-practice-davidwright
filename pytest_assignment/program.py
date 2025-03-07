def divide_numbers(a, b):
    """Returns the result of a divided by b, rounded to two decimals."""
    try:
        result = a / b
        return round(result, 2)
    except ZeroDivisionError:
        return "Division by zero is not allowed. Please enter a non-zero number."
        # Bug: No handling for division by zero

 
def reverse_string(s):
    """Returns the reversed string, with each character's case flipped."""
    s = str(s)
    reversed_s = s[::-1]  # Bug: Might not handle non-string input properly
    flipped_case = ''.join([char.swapcase() for char in reversed_s])
    return flipped_case
 
def get_list_element(lst, index):
    """Returns the element at the given index in the list, or 'Not found' if out of range."""
    if index < 0 or index >= len(lst):  # Bug: Incorrect boundary check
        raise IndexError("Index out of Range")
    else:
        return lst[index]

