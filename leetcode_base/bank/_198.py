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
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [-1] * n

        def dfs(i):
            if i < 0:
                return 0
            if cache[i] != -1:
                return cache[i]
            ans = max(dfs(i - 1), dfs(i - 2) + nums[i])
            cache[i] = ans
            return ans

        return dfs(n - 1)


class _3rd:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * (n + 2)
        for i, x in enumerate(nums):
            f[i + 2] = max(f[i] + x, f[i + 1])
        return f[n + 1]


class _4th:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        f0 = f1 = 0
        for i, x in enumerate(nums):
            f = max(f0 + x, f1)
            f0 = f1
            f1 = f
        return f1


if __name__ == '__main__':
    handlers = [_1st()]
    for handler in handlers:
        print("")
