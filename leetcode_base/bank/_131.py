from typing import List


class _1st:
    # 答案的视角
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        path = []

        def dfs(i: int):
            if i == n:
                ans.append(path.copy())
                return
            for j in range(i, n):
                t = s[i:j + 1]
                if t == t[::-1]:
                    path.append(t)
                    dfs(j + 1)
                    path.pop()

        dfs(0)
        return ans


class _2nd:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []
        n = len(s)

        # start表示当前这段回文子串开始的位置
        def dfs(i: int, start: int) -> None:
            if i == n:
                ans.append(path.copy())
                return
            # 不选 i 和 i+1 之间的逗号（i=n-1 时一定要选）
            if i < n - 1:
                dfs(i + 1, start)
            # 选 i 和 i+1 之间的逗号（把 s[i] 作为子串的最后一个字符）
            t = s[start:i + 1]
            if t == t[::-1]:  # 判断是否是回文
                path.append(t)
                dfs(i + 1, i + 1)  # 当前已经选了，从i+1开始
                path.pop()

        dfs(0, 0)
        return ans


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_2nd()]
    for handler in handlers:
        s = "aab"
        handler.partition(s)
