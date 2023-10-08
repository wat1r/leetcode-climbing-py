from collections import deque
from math import inf
from typing import List


class _1st_1:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        ans = -inf
        q = deque()
        for x, y in points:
            while q and q[0][0] < x - k:
                q.popleft()
            if q:
                ans = max(ans, x + y + q[0][1])
            while q and q[-1][1] <= y - x:
                q.pop()
            q.append((x, y - x))
        return ans


class _1st_2:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        replace = [(c, 1) for c in s]
        for i, src, tar in zip(indices, sources, targets):
            if s.startswith(src, i):  # 判断 s[i:] 的前缀是否为 src，这样写无需切片
                replace[i] = (tar, len(src))  # (替换后的字符串，被替换的长度)

        ans = []
        i = 0
        while i < len(s):
            ans.append(replace[i][0])  # 替换后的字符串（默认为 s[i]）
            i += replace[i][1]  # 被替换的长度（默认为 1）
        return ''.join(ans)

    def test_zip(self):
        names = ['John', 'Amy', 'Jack']
        scores = [98, 100, 85]  # 分数和名字是一一对应的
        for n, s in zip(names, scores):
            print(n, s)


class _1st_3:
    class StockSpanner:

        def __init__(self):
            self.stk = []
            self.cur = 0

        def next(self, price: int) -> int:
            while self.stk and self.stk[-1][1] <= price:
                self.stk.pop()
            prev = self.stk[-1][0] if self.stk else -1
            ans = self.cur - prev
            self.stk.append([self.cur, price])
            self.cur += 1
            return ans


if __name__ == '__main__':
    hs = [_1st_2()]
    for handler in hs:
        s = "abcd"
        indexes = [0, 2]
        sources = ["a", "cd"]
        targets = ["eee", "ffff"]
        # handler.findReplaceString(s, indexes, sources, targets)
        handler.test_zip()
