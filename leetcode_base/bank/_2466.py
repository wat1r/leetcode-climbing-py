from typing import List


class _1st:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10 ** 9 + 7
        f = [1] + [0] * high
        for i in range(1, high + 1):
            if i >= zero:
                f[i] = (f[i] + f[i - zero]) % MOD
            if i >= one:
                f[i] = (f[i] + f[i - one]) % MOD
        return sum(f[low:]) % MOD


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
