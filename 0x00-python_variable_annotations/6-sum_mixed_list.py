#!/usr/bin/env python3
"""
Complex types - Mixed Lists, Union
"""
from typing import List


def sum_mixed_list(mxd_lst: List[int | float]) -> float:
    """
    Type-annotated function sum_mixed_list which takes
    a list mxd_lst of integers and floats and 
    returns their sum as a float
    """
    return float(sum(mxd_lst))
