#!/usr/bin/env python3

"""
In màn hình các số nguyên từ 1 đến 100, nhưng với bội của 3, in ra chữ “Fizz”
thay vì số đo. Với bội của 5, in ra chữ “Buzz” thay vì số đó. Với các số là bội
của cả 3 và 5 thì in ra chữ “FizzBuzz” thay vì số đó. Các số còn lại thì in ra
bình thưòng.
"""


def solve():
    """Thay vì in ra, hãy trả về 1 `list`
    100 phần tử thỏa mãn yêu cầu đề bài

    :rtype: list
    """

    listInteger = []
    for x in range(100):
        integer = x + 1
        if (integer % 3 == 0 and integer % 5 == 0):
            integer = "FizzBuzz"
        elif (integer % 3 == 0):
            integer = "Fizz"
        elif (integer % 5 == 0):
            integer = "Buzz"
        listInteger.append(integer)

    result = listInteger

    # Xóa dòng sau và viết code vào đây set các gía trị phù hợp

    return result


def main():
    for i in solve():
        print(i)


if __name__ == "__main__":
    main()
