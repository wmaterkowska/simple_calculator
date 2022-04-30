#!/bin/python3
import sys
import os
from other_code.add_simple import add

sys.path.append('.')


def test_add_empty():

    s_input = ''
    assert add(s_input) == 0


def test_add_1():

    s_input = '1'
    assert add(s_input) == 1


def test_add_2():
    s_input = '1,3'
    assert add(s_input) == 4
