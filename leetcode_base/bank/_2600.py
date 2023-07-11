from typing import List


class _1st:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        total = 0
        if k <= numOnes:
            total += k
            return total
        total += numOnes
        k -= numOnes
        if k <= numZeros:
            return total
        k -= numZeros
        return total - k


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
