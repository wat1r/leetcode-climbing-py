from cmath import inf
from collections import defaultdict
from typing import List, Optional

from leetcode_base.random_leetcode_step_one import TreeNode


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


class _4th_10:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        # 左侧比nums[i]小（严格,<）的最近的数的下标 minLeft
        # 左侧比nums[i]大（非严格,>=）的最近的数的下标 maxLeft
        minLeft, maxLeft = [0] * n, [0] * n
        minSt, maxSt = [], []
        for i, x in enumerate(nums):
            while minSt and nums[minSt[-1]] > x:
                minSt.pop()
            minLeft[i] = minSt[-1] if minSt else -1
            minSt.append(i)

            while maxSt and nums[maxSt[-1]] <= x:
                maxSt.pop()
            maxLeft[i] = maxSt[-1] if maxSt else -1
            maxSt.append(i)
        # 右侧比nums[i]大（非严格,>=）的最近的数的下标 minRight
        # 右侧比nums[i]小（严格,<）的最近的数的下标 maxRight
        minRight, maxRight = [0] * n, [0] * n
        minSt, maxSt = [], []
        for i in range(n - 1, -1, -1):
            x = nums[i]
            while minSt and nums[minSt[-1]] >= x:
                minSt.pop()
            minRight[i] = minSt[-1] if minSt else n
            minSt.append(i)

            while maxSt and nums[maxSt[-1]] < x:
                maxSt.pop()
            maxRight[i] = maxSt[-1] if maxSt else n
            maxSt.append(i)
        sumMax, sumMin = 0, 0
        for i, x in enumerate(nums):
            sumMax += (maxRight[i] - i) * (i - maxLeft[i]) * x
            sumMin += (minRight[i] - i) * (i - minLeft[i]) * x
        return sumMax - sumMin


class _4th_11:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root: Optional[TreeNode]) -> (int, int):
            if root is None:
                return 0, 0
            coins_l, nodes_l = dfs(root.left)
            coins_r, nodes_r = dfs(root.right)
            coins = coins_l + coins_r + root.val
            nodes = nodes_l + nodes_r + 1
            nonlocal res
            res += abs(coins - nodes)
            return coins, nodes

        dfs(root)
        return res


class _4th_12:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            d = dfs(root.left) + dfs(root.right) + root.val - 1
            nonlocal res
            res += abs(d)
            return d

        dfs(root)
        return res


class _4th_13:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        cur_x, cur_y, cur_dir, ans = 0, 0, 0, 0
        m, n = len(commands), len(obstacles)
        obstacles_set = {(obstacles[i][0], obstacles[i][1]) for i in range(n)}
        for i in range(m):
            if commands[i] == -1:
                cur_dir = (cur_dir + 1) % 4
            elif commands[i] == -2:
                cur_dir = (cur_dir + 3) % 4
            else:
                for j in range(commands[i]):
                    next_x, next_y = cur_x + dirs[cur_dir][0], cur_y + dirs[cur_dir][1]
                    if (next_x, next_y) not in obstacles_set:
                        cur_x = next_x
                        cur_y = next_y
                        ans = max(ans, cur_x * cur_x + cur_y * cur_y)
                    else:
                        break
        return ans


class _4th_14:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degree, g = [0] * n, defaultdict(list)
        for u, v in edges:
            in_degree[u] += 1
            in_degree[v] += 1
            g[u].append(v)
            g[v].append(u)
        q = []
        for i, v in enumerate(in_degree):
            if v <= 1:
                q.append(i)
        while n > 2:
            n -= len(q)
            vs = []
            for u in q:
                for v in g[u]:
                    in_degree[v] -= 1
                    if in_degree[v] == 1:
                        vs.append(v)
            q = vs
        return q


class _4th_15:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        g = [[] for _ in range(len(edges) + 1)]
        for x, y, in edges:
            g[x].append(y)
            g[y].append(x)
        s = {(x, y) for x, y in guesses}

        cnt0 = 0

        def dfs(x: int, fa: int) -> None:
            nonlocal cnt0
            for y in g[x]:
                if y != fa:
                    if (x, y) in s:
                        cnt0 += 1
                    dfs(y, x)

        dfs(0, -1)

        ans = 0

        def reroot(x: int, fa: int, cnt: int) -> None:
            nonlocal ans
            if cnt >= k:
                ans += 1
            for y in g[x]:
                if y != fa:
                    next_cnt = cnt - ((x, y) in s) + ((y, x) in s)
                    reroot(y, x, next_cnt)

        reroot(0, -1, cnt0)
        return ans


class _4th_16:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_s = -inf  # 最大子数组和，不能为空
        max_f = 0
        min_s = 0  # 最小子数组和，可以为空
        min_f = 0
        for x in nums:
            max_f = max(max_f, 0) + x
            max_s = max(max_s, max_f)
            min_f = min(min_f, 0) + x
            min_s = min(min_s, min_f)
        if sum(nums) == min_s:
            return max_s
        return max(max_s, sum(nums) - min_s)


class _4th_17:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        b, ans = nums[-1], 0
        while k:
            ans += b
            b += 1
            k -= 1
        return ans


class _4th_18:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        set_A, set_B = [], []
        n = len(A)
        ans = [0] * n
        for i in range(n):
            a, b = A[i], B[i]
            if i > 0:
                ans[i] = ans[i - 1]
            if a == b:
                ans[i] += 1
            if a in set_B:
                ans[i] += 1
            if b in set_A:
                ans[i] += 1
            set_A.append(a)
            set_B.append(b)
        return ans


if __name__ == '__main__':
    handlers = [_4th_18()]
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
        # handler.sumSubarrayMins([3, 1, 2, 4])
        # handler.maximumOr([8, 1, 2], 2)
        # handler.sumOfPower([2, 1, 4])
        # handler.robotSim([4, -1, 3], [])
        # handler.maximizeSum([1, 2, 3, 4, 5], 3)
        handler.findThePrefixCommonArray([1, 3, 2, 4], [3, 1, 2, 4])
        print("")
