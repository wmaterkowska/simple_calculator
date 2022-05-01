#!/bin/python3
import sys
import os
from other_code.simple_calculator import simple_calculator

sys.path.append('.')

"""
simple tests for different input for __extract_numbers__ and __extract_operators__ functions from simple_calculator class
"""


def test_extract_numbers_input_empty():

    s_input = ''
    assert simple_calculator.__extract_numbers__(s_input) == []


def test_extract_operators_input_empty():

    s_input = ''
    assert simple_calculator.__extract_operators__(s_input) == []


def test_extract_numbers_input_multiple():

    s_input = '1+2+3-2'
    print(simple_calculator.__extract_numbers__(s_input))
    assert simple_calculator.__extract_numbers__(s_input) == [1, 2, 3, 2]


def test_extract_operators_input_multiple():

    s_input = '1+2+3-2'
    print(simple_calculator.__extract_operators__(s_input))
    assert simple_calculator.__extract_operators__(s_input) == ['+', '+', '-']
