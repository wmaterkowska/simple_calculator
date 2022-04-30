#!/bin/python3
"""
    Simple calculator which adds integers separated by '+'

"""


def add(s_input):

    if len(s_input) >= 1:
        #string = s_input.replace('\\n', ',')
        #string = string.replace('\n', ',')
        arr = list(s_input.rstrip().split('+'))
        # print(arr)
        suma = 0
        for i in range(len(arr)):
            suma += int(arr[i])

        return suma

    return 0


if __name__ == "__main__":

    s_inupt = input()

    result = add(s_inupt)
    print(result)
