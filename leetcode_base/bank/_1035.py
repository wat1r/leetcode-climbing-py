from typing import List


class _1st:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                f[i][j] = f[i - 1][j - 1] + 1 if nums1[i - 1] == nums2[j - 1] else max(f[i - 1][j], f[i][j - 1])
        return f[m][n]


class _2nd:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i, x in enumerate(nums1):
            for j, y in enumerate(nums2):
                f[i + 1][j + 1] = f[i][j] + 1 if x == y else max(f[i][j + 1], f[i + 1][j])
        return f[m][n]


class _3rd:
    print("")


class _4th:
    print("")
