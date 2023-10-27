from typing import List


class _1st:
    def generateParenthesis(self, n: int) -> List[str]:
        m = 2 * n
        ans = []
        path = [''] * m

        def dfs(i, open):
            if i == m:
                ans.append(''.join(path))
                return
            if open < n:
                path[i] = '('
                dfs(i + 1, open + 1)
            if i - open < open:
                path[i] = ')'
                dfs(i + 1, open)

        dfs(0, 0)
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
