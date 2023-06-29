from typing import List


class _1st:
    # f[i][0]：当数值 i 不被选择，那么前一个数「可选/可不选」，在两者中取 max 即可。
    # f[i][1]：当数值 i 被选，那么前一个数只能「不选」，同时为了总和最大数值 i 要选就全部选完。
    def deleteAndEarn(self, nums: List[int]) -> int:
        N = 10010
        cnt = [0] * N
        mmax = 0
        for x in nums:
            cnt[x] += 1
            mmax = max(mmax, x)
        f = [[0] * 2 for _ in range(mmax + 1)]
        for i in range(mmax + 1):
            f[i][0] = max(f[i - 1][1], f[i - 1][0])
            f[i][1] = f[i - 1][0] + i * cnt[i]
        return max(f[mmax])


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
