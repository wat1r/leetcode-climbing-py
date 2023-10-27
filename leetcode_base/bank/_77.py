from typing import List


class _1st:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i: int):
            d = k - len(path)
            if i < d:
                return
            if len(path) == k:
                ans.append(path.copy())
                return

            for j in range(i, d - 1, -1):
                path.append(j)
                dfs(j - 1)
                path.pop()

        dfs(n)
        return ans


class _2nd:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i: int):
            d = k - len(path)
            if d == 0:
                ans.append(path.copy())
                return
            if i > d:
                dfs(i - 1)
            path.append(i)
            dfs(i - 1)
            path.pop()

        dfs(n)
        return ans


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_1st()]
    for handler in handlers:
        print("")
