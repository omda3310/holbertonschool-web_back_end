#!/usr/bin/env python3
"""Annotated function sum_mixed_list"""


from typing import List, Union
mx_list = Union[int, float]


def sum_mixed_list(mxd_lst: List[mx_list]) -> float:
    """ Returns their sum as a float"""
    return sum(mxd_lst)
