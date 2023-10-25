from typing import List

M = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]


class _1st:

    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []
        ans = []
        path = [''] * n

        def dfs(i: int):
            if i == n:
                ans.append(''.join(path))
                return
            for c in M[int(digits[i])]:
                path[i] = c
                dfs(i + 1)

        dfs(0)
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
        handler.letterCombinations("23")
        print("")
