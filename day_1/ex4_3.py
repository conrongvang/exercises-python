#!/usr/bin/env python3
import string

def solve(words):
    """Trả về list chứa điểm tương ứng của các từ trong `words`

    Nếu a b c d (không phân biệt chữ hoa thường) .... lần lượt bằng 1 2 3 4 ...
    thì từ ``attitude`` có giá trị bằng 100.

    Gợi ý::

      import string
      print(string.ascii_lowercase)
    """

    result = []

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    ordinal = []
    sum2 = 0
    tamp2 = 0
    for index in range(len(string.ascii_lowercase)):
        ordinal.append(index+1)
    print("ordinal: ",ordinal, "\n")
    length = len(words)
    # return result


def main():
    words = [
        "numpy",
        "django",
        "saltstack",
        "discipline",
        "Python",
        "FAMILUG",
        "pymi",
    ]

    print(solve(words))


if __name__ == "__main__":
    main()
