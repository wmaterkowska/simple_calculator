#!/bin/python3
import sys
import os
from other_code.simple_calculator import addition, subtraction

sys.path.append('.')


def test__add_input_empty():

    s_input = ''
    assert addition(s_input) == 0


def test_add_input_one():

    s_input = '1'
    assert addition(s_input) == 1


def test__sub_input_empty():

    s_input = ''
    assert subtraction(s_input) == 0


def test_sub_input_one():

    s_input = '1'
    assert subtraction(s_input) == 1
