#!/bin/python3

import re

"""
    Simple calculator which adds integers separated by '+'

"""


class simple_calculator:

    def __init__(self, s_input):
        self.s_input = s_input

    def __extract_numbers__(s_input):
        if s_input == '':
            return []
        else:
            temp_string = s_input.replace('-', '+')
            numbers = list(map(int, temp_string.rstrip().split('+')))
            return numbers

    def __extract_operators__(s_input):
        operators = []
        for sign in s_input:
            if sign == '-' or sign == '+':
                operators.append(sign)
        return operators

    def calculate(s_input):
        """
        main calculator method for subtraction and addition
        """
        numbers = simple_calculator.__extract_numbers__(s_input)
        operators = simple_calculator.__extract_operators__(s_input)

        if numbers == []:
            return 0

        result = numbers[0]
        for number, operator in zip(numbers[1:], operators):
            if operator == '+':
                result += number
            else:
                result -= number

        return result

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

    #add_result = simple_calculator.addition(s_input)
    # print(add_result)

    #sub_result = simple_calculator.subtraction(s_input)
    # print(sub_result)

    print(simple_calculator.calculate(s_input))
