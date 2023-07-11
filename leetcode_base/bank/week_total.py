from cmath import inf

from linecache import cache
from typing import List

from nltk import pairwise


class _1st:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def dfs(i):
            if i == 0:
                return 0
            res = -inf
            for j in range(i):
                if -target <= nums[i] - nums[j] <= target:
                    res = max(res, dfs(j) + 1)
            return res

        res = dfs(n - 1)
        return -1 if res < 0 else res


class _2nd:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        f = [-inf] * n
        f[0] = 0
        for i in range(1, n):
            for j in range(i):
                if -target <= nums[i] - nums[j] <= target:
                    f[i] = max(f[i], f[j] + 1)
        return -1 if f[n - 1] < 0 else f[n - 1]


class _3rd:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        nums = (nums1, nums2)

        # dfs(i , j ) 表示以numsj[i]结尾的最长非递减子数组的长度
        @cache
        def dfs(i, j):
            if i == 0:
                return 1
            res = 1
            if nums1[i - 1] <= nums[j][i]:
                res = dfs(i - 1, j) + 1
            if nums2[i - 1] <= nums[j][i]:
                res = max(res, dfs(i - 1, j) + 1)
            return res

        return max(dfs(i, j) for j in range(2) for i in range(n))


class _4th:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        nums = (nums1, nums2)
        f = [[1, 1] for _ in range(n)]
        for i in range(1, n):
            for j in range(2):
                if nums1[i - 1] <= nums[j][i]:
                    f[i][j] = f[i - 1][0] + 1
                if nums2[i - 1] <= nums[j][i]:
                    f[i][j] = max(f[i][j], f[i - 1][1] + 1)
        return max(map(max, f))


class _4th_1:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        ans = f0 = f1 = 1
        for (x0, y0), (x1, y1) in pairwise(zip(nums1, nums2)):
            f = g = 1
            if x0 <= x1: f = f0 + 1
            if y0 <= x1: f = max(f, f1 + 1)
            if x0 <= y1: g = f0 + 1
            if y0 <= y1: g = max(g, f1 + 1)
            f0, f1 = f, g
            ans = max(ans, f0, f1)
        return ans


class _4th_2:
    def alternatingSubarray(self, nums: List[int]) -> int:
        ans = -1
        i, n = 0, len(nums)
        while i < n - 1:
            if nums[i + 1] - nums[i] != 1:
                i += 1
                continue
            i0 = i
            i += 1
            while i < n and nums[i] == nums[i0] + (i - i0) % 2:
                i += 1
            ans = max(ans, i - i0)
            i -= 1
        return ans


class _4th_3:
    def bin_gen(self):
        tmp = set()
        for i in range(30):
            x = bin(pow(5, i))[2:]
            if len(x) > 15: break
            tmp.add(x)

    tmp = set()
    for i in range(10):
        x = bin(pow(5, i))[2:]
        if len(x) > 15: break
        tmp.add(x)

    def minimumBeautifulSubstrings(self, s: str) -> int:
        n = len(s)

        @cache
        def dfs(i):
            if i == n:
                return 0
            res = inf
            for j in range(i + 1, n + 1):
                if s[i:j] in self.tmp:
                    res = min(res, dfs(j) + 1)
            return res

        res = dfs(0)
        return -1 if res == inf else res


class _4th_4:

    def minimumBeautifulSubstrings(self, s: str) -> int:
        candidates = []
        for k in range(10):
            x = bin(pow(5, k))[2:]
            if len(x) > 15:
                break
            candidates.append(x)

        n = len(s)

        @cache
        def dfs(i):
            if i == 0:
                return 0
            res = inf
            for j in range(i - 1, -1, -1):
                if s[j:i] in candidates:
                    res = min(res, dfs(j) + 1)
            return res

        res = dfs(n)
        return -1 if res == inf else res


class _4th_5:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        candidates = []
        for k in range(10):
            x = bin(pow(5, k))[2:]
            if len(x) > 15:
                break
            candidates.append(x)
        n = len(s)
        f = [inf] * n + [0]
        for i in range(n - 1, -1, -1):
            # 加速
            if s[i] == '0':
                continue
            for t in candidates:
                if i + len(t) > n:
                    break
                if s[i:i + len(t)] == t:
                    f[i] = min(f[i], f[i + len(t)] + 1)
        return f[0] if f[0] < inf else -1


if __name__ == '__main__':
    handlers = [_4th_5()]
    for handler in handlers:
        # nums1 = [2, 3, 1]
        # nums2 = [1, 2, 1]
        # handler.maxNonDecreasingLength(nums1, nums2)
        # nums = [2, 3, 4, 3, 4]
        # handler.alternatingSubarray(nums)
        # handler.bin_gen()
        handler.minimumBeautifulSubstrings("1011")
        print()
