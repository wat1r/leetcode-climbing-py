from typing import List


class _1st:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        ans = pre = cur = 0
        for i, c in enumerate(s):
            cur += 1
            if i == len(s) - 1 or c != s[i + 1]:
                if c == '1':
                    ans = max(ans, min(pre, cur) * 2)
                pre = cur
                cur = 0
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
        handler.findTheLongestBalancedSubstring("01000111")
