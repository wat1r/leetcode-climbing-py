from typing import List
import numpy


class _1st:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        t = len(strs)
        f = numpy.empty((t + 1, m + 1, n + 1))
        for i in range(1, t + 1):
            c = self.get_cnt(strs[i - 1])
            zeros, ones = c[0], c[1]
            for j in range(1, m + 1):
                for k in range(1, n + 1):
                    f[i][j][k] = f[i - 1][j][k]
                    if j >= zeros and k >= ones:
                        f[i][j][k] = max(f[i][j][k], f[i - 1][j - zeros][k - ones] + 1)
        return f[t][m][n]

    def get_cnt(self, s: str):
        cnt = [0, 0]
        for x in list(s):
            cnt[ord(x) - ord('0')] += 1
        return cnt


class _2nd:
    print("")


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_1st()]
    for handler in handlers:
        handler.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3)
