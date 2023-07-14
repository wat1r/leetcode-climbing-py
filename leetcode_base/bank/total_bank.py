from cmath import inf
from collections import defaultdict
from typing import List


class _1st:
    def alternateDigitSum(self, n: int) -> int:
        l = len(str(n))
        res, d = 0, 1
        if l % 2 == 0:
            d = -1
        while n > 0:
            res += (n % 10) * d
            n //= 10
            d = -d
        return res


class _1st_1:
    def alternateDigitSum(self, n: int) -> int:
        res, sign = 0, 1
        while n:
            res += n % 10 * sign
            n //= 10
            sign = -sign
        return res * -sign


class UnionFind:
    def __init__(self, n) -> None:
        self.p = [x for x in range(n)]
        self.size = [1 for _ in range(n)]
        self.part = n

    def find(self, x: int):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def merge(self, x, y) -> bool:
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        if self.size[root_x] > self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.p[root_x] = root_y
        self.size[root_y] += self.size[root_x]
        self.part -= 1
        return True


class _2nd:

    def largestComponentSize(self, nums: List[int]) -> int:
        n = max(nums)
        uf = UnionFind(n + 1)
        for x in nums:
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    uf.merge(x, x // i)
                    uf.merge(x, i)
        # 下面写法超时
        # for j, x in enumerate(nums):
        #     print(j, x)
        #     k = x
        #     for i in range(2, x // 2 + 1, 1):
        #         flag = False
        #         while x % i == 0:
        #             x //= i
        #             flag = True
        #         if flag:
        #             uf.merge(k, i)
        #         # print(i)
        #     if x > 1:
        #         uf.merge(k, x)
        dic = defaultdict(int)
        for x in nums:
            dic[uf.find(x)] += 1
        return max(dic.values())


class _3rd:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        uf = UnionFind(n + 1)
        for i in range(threshold + 1, n + 1):
            for j in range(2 * i, n + 1, i):
                print(i, j)
                uf.merge(i, j)
        res = []
        for q in queries:
            u, v = q[0], q[1]
            res.append(uf.find(u) == uf.find(v))
        return res


class _4th:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(x: int, y: int) -> int:
            return x if y == 0 else gcd(y, x % y)

        x, y = max(nums), min(nums)
        return gcd(x, y)


class _4th_1:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a: int, b: int) -> int:
            return a if b == 0 else gcd(b, a % b)

        l = gcd(len(str1), len(str2))
        res = str1[:l]
        if str1 + str2 == str2 + str1:
            return res
        return ''


class _4th_2:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        print("")


class _4th_4:
    def matrixSum(self, nums: List[List[int]]) -> int:
        m, n = len(nums), len(nums[0])
        res = 0
        for i in range(m):
            nums[i].sort()
            # sorted(nums, key=lambda x: nums[i])
        for j in range(n):
            mmax = 0
            for i in range(m):
                mmax = max(mmax, nums[i][j])
            res += mmax
        return res


class _4th_5:
    def maximumOr(self, nums: List[int], k: int) -> int:
        n = len(nums)
        suf = [0] * (n + 1)
        for i in range(n - 1, 0, -1):
            suf[i] = suf[i + 1] | nums[i]
        res = pre = 0
        for i, x in enumerate(nums):
            res = max(res, pre | x << k | suf[i + 1])
            pre |= x
        return res


class _3rd_6:
    def sumOfPower(self, nums: List[int]) -> int:
        nums.sort()
        MOD = 10 ** 9 + 7
        ans = s = 0
        for x in nums:
            ans = (ans + x * x * (x + s)) % MOD
            s = (2 * s + x) % MOD
        return ans
        # n = len(nums)
        # max_suf, min_suf = [-inf] * (n + 1), [inf] * (n + 1)
        # for i in range(n):
        #     max_suf[i + 1] = max(max_suf[i], nums[i])
        #     min_suf[i + 1] = min(min_suf[i], nums[i])


class _4th_6:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(arr)
        # 左边界left[i]为左侧严格小于arr[i]的最近元素的位置(不存在时为-1)
        left, st = [-1] * n, []
        for i, x in enumerate(arr):
            while st and arr[st[-1]] >= x:
                st.pop()  # 移除大于x的元素
            if st:
                left[i] = st[-1]
            st.append(i)
        # 右边界right[i]为右侧小于等于arr[i]的最近元素的位置(不存在时为n)
        right, st = [n] * n, []
        for i in range(n - 1, -1, -1):
            while st and arr[st[-1]] > arr[i]:
                st.pop()
            if st:
                right[i] = st[-1]
            st.append(i)
        ans = 0
        for i, (x, l, r) in enumerate(zip(arr, left, right)):
            ans += x * (i - l) * (r - i)
        return ans % MOD


class _4th_7:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(arr)
        # 左边界left[i]为左侧严格小于arr[i]的最近元素的位置(不存在时为-1)
        # 右边界right[i]为右侧小于等于arr[i]的最近元素的位置(不存在时为n)
        left, right, st = [-1] * n, [n] * n, []
        for i, x in enumerate(arr):
            while st and arr[st[-1]] >= x:
                right[st.pop()] = i  # 移除大于x的元素
            if st:
                left[i] = st[-1]
            st.append(i)

        ans = 0
        for i, (x, l, r) in enumerate(zip(arr, left, right)):
            ans += x * (i - l) * (r - i)
        return ans % MOD


class _4th_8:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        arr.append(-1)
        ans, st = 0, [-1]
        for r, x in enumerate(arr):
            while len(st) > 1 and arr[st[-1]] >= x:
                i = st.pop()
                ans += arr[i] * (i - st[-1]) * (r - i)
            st.append(r)
        return ans % MOD


class _4th_9:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        left, right, st = [0] * n, [n - 1] * n, []
        for i, x in enumerate(nums):
            while st and nums[st[-1]] >= x:
                # right[i]是非严格的右侧最近的小于等于nums[i]的元素下标
                right[st[-1]] = i - 1
                st.pop()
            if st:
                # left[i]是左侧最近的严格小于nums[i]的元素下标
                left[i] = st[-1] + 1
            st.append(i)
        pre = [0]
        for i, x in enumerate(nums):
            pre.append(pre[-1] + x)
        ans = max((pre[right[i] + 1] - pre[left[i]]) * x for i, x in enumerate(nums))
        return ans % MOD


if __name__ == '__main__':
    handlers = [_4th_5()]
    for handler in handlers:
        # handler.largestComponentSize([4, 6, 15, 35])
        # handler.largestComponentSize()
        # handler.areConnected(6, 2, [[1, 4], [2, 5], [3, 6]])
        # handler.areConnected(6, 0, [[4, 5], [3, 4], [3, 2], [2, 6], [1, 3]])
        # handler.areConnected(5, 1, [[4, 5], [4, 5], [3, 2], [2, 3], [3, 4]])
        # handler.gcdOfStrings("ABCABC", "ABC")
        # handler.matrixSum([[2, 7, 1], [6, 4, 2], [6, 5, 3], [3, 2, 1]])
        # handler.maximumOr([12, 9], 1)
        # handler.maximumOr([8, 1, 2], 2)
        handler.sumSubarrayMins([3, 1, 2, 4])
        # handler.maximumOr([8, 1, 2], 2)
        handler.sumOfPower([2, 1, 4])
        print("")
