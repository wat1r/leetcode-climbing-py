from typing import List


class _1st:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        f = [[0] * 2 for _ in range(n + 1)]  # 0表示不偷当前房间，1表示偷当前房间
        for i in range(1, n + 1):
            f[i][0] = max(f[i - 1][0], f[i - 1][1])
            f[i][1] = f[i - 1][0] + nums[i - 1]
        return max(f[n])


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
