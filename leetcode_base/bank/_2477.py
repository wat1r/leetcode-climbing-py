from typing import List


# https://leetcode.cn/problems/minimum-fuel-cost-to-report-to-the-capital/?envType=daily-question&envId=2023-12-05
class _1st:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        g = [[] for _ in range(len(roads) + 1)]
        for u, v in roads:
            g[u].append(v)
            g[v].append(u)

        ans = 0

        def dfs(x: int, fa: int) -> int:
            size = 1
            for y in g[x]:
                if y != fa:
                    size += dfs(y, x)

            if x:
                nonlocal ans
                ans += (size - 1) // seats + 1
            return size

        dfs(0, -1)
        return ans


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
