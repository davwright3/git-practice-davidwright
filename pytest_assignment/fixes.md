# List of found bugs and fixes

## divide_numbers function

Bug: No error handling for dividing by zero, instead would cause system crash.
Fix: Used try/except to check for divide by zero errors, printed statement for user to see that the code is invalid.

## reverse_string function

Bug: Original code not able to handle arguments passed in forms other than string.
Fix: Added helper to convert any entered variable into a string before handling the string reversal. 

## get_list_element
Bug: Original code allows for negative index checking, which is not what the method is designed for.
Fix: 
