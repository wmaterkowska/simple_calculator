#!/bin/python3
from other_code.add_simple import add

import os
import sys
sys.path.append('../')


def test_add_unknown():

    s_input = '1,2,3,4'
    assert add(s_input) == 10


def test_add_unknown2():

    s_input = '1,2,3,4,5,6,7,8,9'
    assert add(s_input) == 45


def test_add_newline():

    s_input = '1\n2,3'
    assert add(s_input) == 6


def test_add_newline2():

    s_input = '1\n2'
    assert add(s_input) == 3
