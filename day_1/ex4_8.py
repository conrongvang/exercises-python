#!/usr/bin/env python3


def solve():
    """Trả về list N bộ integer (a, b, c) là độ dài 3 cạnh của tam giác vuông
    cạnh huyền `c` có chu vi 24 cm (perimeter), biết độ dài các cạnh <= 10cm.

    Yêu cầu dùng list comprehension.
    """

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    listN = [
        (a,b,c)
        for a in range(1,11,1)
        for b in range(1,11,1)
        for c in range(1,11,1)
        if ((a+b+c == 24) and (a*a + b*b == c*c))
    ]

    result = listN

    return result

def main():
    print(solve())


if __name__ == "__main__":
    main()
