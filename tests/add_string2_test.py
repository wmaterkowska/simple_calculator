#!/bin/python3
from other_code.simple_calculator import addition, subtraction

import os
import sys
sys.path.append('../')


def test_add_unknown():

    s_input = '1+2+3+4'
    assert addition(s_input) == 10


def test_add_unknown2():

    s_input = '1+2+3+4+5+6+7+8+9'
    assert addition(s_input) == 45


def test_subtract_unknown():

    s_input = '2-1'
    assert subtraction(s_input) == 1
