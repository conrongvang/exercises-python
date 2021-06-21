#!/usr/bin/env python3


__doc__ = """
Yêu cầu:
- Viết chương trình cứ 1 giây in ra màn hình thời gian hiện tại.
- Sau N lần thì chương trình kết thúc

Gợi ý:
time.sleep, datetime.datetime.now

Đọc thêm logging: https://pymotw.com/3/logging/index.html
"""

import time
import datetime  # NOQA
from typing import List, Tuple

import log

logger = log.get_logger(__name__)


def your_function(N: int) -> Tuple[List[str], float]:
    """Trả về tuple chứa 2 phần tử bao gồm:
    - List chứa các điểm thời gian (string) sau N lần thực hiện
    theo yêu cầu từ ``__doc__``
    - Tổng thời gian chạy của function

    :rtype tuple:
    """
    # Sửa tên và function cho phù hợp, trả về kết quả yêu cầu.
    start = time.time()
    # NOTE: DO NOT FORMAT log by % or .format
    # http://www.familug.org/2014/09/python-logging-ung-format-log-message.html
    logger.debug("Start at %f", start)

    result: List[str] = []
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    raise NotImplementedError("Bạn chưa làm bài này")

    end = time.time()
    logger.debug("End at %f", end)
    total_time = end - start
    return (result, total_time)


def solve(N: int) -> Tuple:
    """không cần chỉnh sửa trong hàm solve, chỉ thực hiện
    đổi tên lại function của mình cho phù hợp

    Hàm solve dùng cho mục đích `test`
    :rtype tuple:
    """
    result = your_function(N)
    return result


def main() -> None:
    print(solve(5))


# __name__ là một biến|name đặc biệt do Python tự tạo ra
# nó có giá trị là string "__main__" khi file được chạy bằng lệnh
# python filename.py
# và có giá trị là tên file (bỏ .py) khi được import.
if __name__ == "__main__":
    print(__name__)
    main()