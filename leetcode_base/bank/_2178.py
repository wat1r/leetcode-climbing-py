from typing import List


class _1st:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        res = []
        if finalSum % 2 == 1:
            return res
        i = 2
        while i <= finalSum:
            finalSum -= i
            res.append(i)
            i += 2
        res[-1] += finalSum
        return res


class _2nd:
    print("")


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_1st()]
    for handler in handlers:
        print("")
