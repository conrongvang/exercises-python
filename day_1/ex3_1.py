#!/usr/bin/env python3
data = 1000


def solve(input_data):
    """Đầu vào: một số nguyên dương

    Đầu ra: số nguyên tạo bởi phần từ số 1 cuối cùng trở về bên
    phải - của dạng binary của số đầu vào.

    Ví dụ::

      input_data = 5 # (0b101)
      output = 1

      input_data = 24 (11000)
      output = 1000

      input_data = 9 (1001)
      output = 1

    Hàm có sẵn: bin(10) == '0b1010'
    Hàm có sẵn tạo ra integer từ string: 69 == int('69')
    """

    binary = bin(input_data)
    length = len(binary)
    last = 0
    concatenation = ""
    for index in range(length):
        if(binary[index] == "1"):
            last = index
    if(last != (length-1)):
        concatenation = binary[last:]

    result = concatenation
    # Xoá dòng raise và Viết code vào đây set result làm kết quả

    return result


def main():
    print(solve(data))


if __name__ == "__main__":
    main()
