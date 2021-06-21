#!/usr/bin/env python3

"""
Viết chương trình loại bỏ phần mở rộng của một tên file bất kỳ.

Ví dụ::

  input_data = '....slsslslsls...sls'
  output = '....slsslslsls..'

  input_data = 'maria.data.mp9'
  output = 'maria.data'

Read: https://docs.python.org/3/library/stdtypes.html#str.rfind
"""


def solve(input_data):
    """Trả về tên file sau khi loại bỏ phần mở rộng

    :param input_data: tên file bất kì
    :rtype: str
    """
    length = len(input_data)
    last = 0
    result = None
    print()
    if ("." in input_data):
        for index in range(length):
                if (input_data[index] == "."):
                    last = index
        result = input_data[:last]
    else:
        result = "This file is not exist extend."


    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp

    return result


def main():
    data = "maria.data.mp9"
    print(solve(data))


if __name__ == "__main__":
    main()
