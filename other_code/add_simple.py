#!/bin/python3
"""
    String calculator which adds integers separated by ',' or '\n'

"""


def add(s_input):

    if len(s_input) >= 1:
        string = s_input.replace('\\n', ',')
        string = string.replace('\n', ',')
        arr = list(string.rstrip().split(','))
        print(arr)
        suma = 0
        for i in range(len(arr)):
            suma += int(arr[i])

        return suma

    return 0


if __name__ == "__main__":

    s_inupt = input()
    print(s_inupt)

    result = add(s_inupt)
    print(result)
