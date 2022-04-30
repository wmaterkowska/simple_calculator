#!/bin/python3
from other_code.simple_calculator import simple_calculator

import os
import sys
sys.path.append('../')


def test_add_unknown():

    s_input = '1+2+3+4'
    assert simple_calculator.addition(s_input) == 10


def test_add_unknown2():

    s_input = '1+2+3+4+5+6+7+8+9'
    assert simple_calculator.addition(s_input) == 45


def test_subtract_unknown():

    s_input = '2-1'
    assert simple_calculator.subtraction(s_input) == 1
