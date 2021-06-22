#!/usr/bin/env python3

import time


def solve():
    """Tính số nghiệm của bài toán lớp 3

    Với các biến a,b,c,d,e,f,g,h,i là các số nằm trong khoảng 1-9 (các biến có
    thể có giá trị giống nhau), dạng biểu thức:

      a + 13 * b / c + d + 12 * e - f - 11 + g * h / i - 10 = 66
    """

    start = time.time()

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    result = [
        (a, b, c, d, e, f, g, h, i)
        for a in range(1, 10, 1)
        for b in range(1, 10, 1)
        for c in range(1, 10, 1)
        for d in range(1, 10, 1)
        for e in range(1, 10, 1)
        for f in range(1, 10, 1)
        for g in range(1, 10, 1)
        for h in range(1, 10, 1)
        for i in range(1, 10, 1)
        if (a + 13 * b / c + d + 12 * e - f - 11 + g * h / i - 10 == 66)
    ]

    print(result)
    print("Took: {}".format(time.time() - start))


def main():
    solve()

if __name__ == "__main__":
    main()
