#!/bin/python3
"""
    Simple calculator which adds integers separated by '+'

"""


def addition(s_input):

    if len(s_input) >= 1:
        arr_add = list(s_input.rstrip().split('+'))
        # print(arr_add)
        result_add = 0
        for i in range(len(arr_add)):
            result_add += int(arr_add[i])

        return result_add

    return 0


def subtraction(s_input):

    if len(s_input) >= 1:
        arr_sub = list(s_input.rstrip().split('-'))
        # print(arr_sub)
        result_sub = int(arr_sub[0])
        for i in range(1, len(arr_sub)):
            result_sub -= int(arr_sub[i])

        return result_sub

    return 0


if __name__ == "__main__":

    s_input = input()

    add_result = addition(s_input)
    print(add_result)

    sub_result = subtraction(s_input)
    print(sub_result)
