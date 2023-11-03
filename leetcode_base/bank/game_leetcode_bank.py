import collections
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


class _1st_4:
    def splitNum(self, num: int) -> int:
        s = sorted(str(num))
        res = int(''.join(s[::2])) + int(''.join(s[1::2]))
        return res


class _1st_5:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = collections.defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1
            m[tuple(counts)].append(s)
        return list(m.values())


class _1st_6:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str],
                    student_id: List[int], k: int) -> List[int]:
        score = collections.defaultdict(int)
        for w in positive_feedback: score[w] = 3
        for w in negative_feedback: score[w] = -1
        stu = []
        for r, i in zip(report, student_id):
            s = 0
            for w in r.split():
                s += score[w]
            stu.append((-s, i))
        stu.sort()
        # a = sorted((-sum(score[w] for w in r.split()), i) for r, i in zip(report, student_id))
        return [i for _, i in stu[:k]]


class _1st_7:
    def countPoints(self, s: str) -> int:
        n, ans = len(s), 0
        map = [0] * 128
        for i in range(0, n, 2):
            map[ord(s[i]) - ord('B')] |= 1 << (int(s[i + 1]) - int('0'))
        for i in range(10):
            tot = 0
            for c in ['R', 'G', 'B']:
                tot += (map[ord(c) - ord('B')] >> i) & 1
            ans += 1 if tot == 3 else 0
        return ans


if __name__ == '__main__':
    hs = [_1st_7()]
    for handler in hs:
        # s = "abcd"
        # indexes = [0, 2]
        # sources = ["a", "cd"]
        # targets = ["eee", "ffff"]
        # handler.findReplaceString(s, indexes, sources, targets)
        # handler.test_zip()
        # num = 4325
        # handler.splitNum(num)
        # strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        # handler.groupAnagrams(strs)
        # positive_feedback = ["smart", "brilliant", "studious"]
        # negative_feedback = ["not"]
        # report = ["this student is studious", "the student is smart"]
        # student_id = [1, 2]
        # k = 2
        # handler.topStudents(positive_feedback, negative_feedback, report, student_id, k)
        rings = "B0B6G0R6R0R6G9"
        handler.countPoints(rings)