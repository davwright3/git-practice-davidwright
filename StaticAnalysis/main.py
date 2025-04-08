"""Module iterates list of numbers and appends the factor of the number"""

import math
from line_profiler import LineProfiler




def slow_func(lst):
    """Function receives a list of numbers as an input and returns the number factored to 1000"""
    factor = math.prod([999, 1000])//2
    return [i*factor for i in lst]


def main():
    """Main function of module"""
    lp = LineProfiler()
    numbers = list(range(1000))
    lp_wrapper = lp(slow_func)
    lp_wrapper(numbers)
    lp.print_stats()
    output = slow_func(numbers)
    print("Result: ", output)


if __name__ == "__main__":
    main()
