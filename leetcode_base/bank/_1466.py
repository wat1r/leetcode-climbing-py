from typing import List


class _1st:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y in connections:
            g[x].append([y, 1])  # 1标记原方向的边
            g[y].append([x, 0])  # 0标记反向边

        def dfs(x: int, fa: int) -> int:
            ans = 0
            for e in g[x]:
                y = e[0]
                if y != fa:
                    ans += e[1] + dfs(y, x)
            return ans

        return dfs(0, -1)


class _2nd:
    print("")


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_1st()]
    for handler in handlers:
        n = 3
        c = [[1, 0], [2, 0]]
        handler.minReorder(n, c)
