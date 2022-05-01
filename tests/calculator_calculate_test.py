#!/bin/python3
from other_code.simple_calculator import simple_calculator

import os
import sys
sys.path.append('../')

"""
simple tests for different input for calculate function from simple_calculator class
"""


def test_calculate_simple_addition():
    s_input = '2+3'
    assert simple_calculator.calculate(s_input) == 5


def test_calculate_simple_subtraction():
    s_input = '3-2'
    assert simple_calculator.calculate(s_input) == 1


def test_calculate_multiple_addition():
    s_input = '1+2+3+4+5'
    assert simple_calculator.calculate(s_input) == 15


def test_calculate_multiple_subtraction():
    s_input = '24-9-8'
    assert simple_calculator.calculate(s_input) == 7


def test_calculate_mixed_addition_subtraction():
    s_input = '5+3-4+7+2-6'
    assert simple_calculator.calculate(s_input) == 7
