from typing import List


class _1st:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        M, N = len(heights), len(heights[0])
        dsu = DSU()
        g = []
        for i in range(M):
            for j in range(N):
                pos = i * N + j
                if i < M - 1:
                    g.append([abs(heights[i + 1][j] - heights[i][j]), pos, pos + N])
                if j < N - 1:
                    g.append([abs(heights[i][j + 1] - heights[i][j]), pos, pos + 1])
        g.sort()
        for e in g:
            dsu.union(e[1], e[2])
            if dsu.connected(0, M * N - 1):
                return e[0]
        return 0


class DSU:
    def __init__(self):
        self.par = list(range(10001))

    def find(self, x):
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        self.par[self.find(x)] = self.find(y)

    def connected(self, x, y):
        return self.find(x) == self.find(y)


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
