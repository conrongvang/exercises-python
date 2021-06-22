#!/usr/bin/env python3


def solve(numbers):
    """Tìm phần tử lớn nhất của list số nguyên `numbers`
    Không sử dụng function `max`, `sorted`

    Gợi ý: python có sẵn giá trị âm/dương vô cùng.
    """
    assert isinstance(numbers, list)
    

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    max = 0
    for i in numbers:
        if (i > max):
            max = i
    result = max
    return result


def main():
    print(solve([-1, 5, 9, 6, -999999999999999, 1]))


if __name__ == "__main__":
    main()
