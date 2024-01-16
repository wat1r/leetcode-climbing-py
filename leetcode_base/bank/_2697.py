from typing import List


class _1st:
    def makeSmallestPalindrome(self, s: str) -> str:
        l, r = 0, len(s) - 1
        t = list(s)
        while l < r:
            if t[l] != t[r]:
                if t[l] < t[r]:
                    t[r] = t[l]
                else:
                    t[l] = t[r]
            l += 1
            r -= 1
        return ''.join(t)


class _2nd:
    def makeSmallestPalindrome(self, s: str) -> str:
        l, r = 0, len(s) - 1
        t = list(s)
        while l < r:
            if t[l] != t[r]:
                t[l] = t[r] = min(t[l], t[r])
            l += 1
            r -= 1
        return ''.join(t)


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_1st()]
    for handler in handlers:
        print("")
