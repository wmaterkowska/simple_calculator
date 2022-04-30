#!/bin/python3
import sys
import os
from other_code.add_simple import add

sys.path.append('.')


def test__add_input_empty():

    s_input = ''
    assert add(s_input) == 0


def test_add_input_one():

    s_input = '1'
    assert add(s_input) == 1
