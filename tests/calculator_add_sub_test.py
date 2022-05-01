#!/bin/python3
from other_code.simple_calculator import simple_calculator

import os
import sys
sys.path.append('../')


"""
simple tests for addition and subtraction functions from simple_calculator class
"""


def test_addition_4numbers():

    s_input = '1+2+3+4'
    assert simple_calculator.addition(s_input) == 10


def test_addition_multiple():

    s_input = '1+2+3+4+5+6+7+8+9'
    assert simple_calculator.addition(s_input) == 45


def test_subtraction_simple():

    s_input = '2-1'
    assert simple_calculator.subtraction(s_input) == 1


def test_subtraction_4numbers():

    s_input = '5-4-3-2'
    assert simple_calculator.subtraction(s_input) == -4
