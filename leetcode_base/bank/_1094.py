from itertools import accumulate
from typing import List


class _1st:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        d = [0] * 1001
        for num, _from, _to in trips:
            d[_from] += num
            d[_to] -= num
        a = [0] * 1001
        for i, x in enumerate(d):
            a[i] = d[i] if i == 0 else d[i] + a[i - 1]
        for x in a:
            if x > capacity:
                return False
        return True


class _2nd:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        d = [0] * 1001
        for num, _from, _to in trips:
            d[_from] += num
            d[_to] -= num
        return all(x <= capacity for x in accumulate(d))


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_1st()]
    for handler in handlers:
        print("")
