from typing import List


class _1st:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = []
        for x in intervals:
            if not ans or ans[-1][1] < x[0]:
                ans.append(x)
            else:
                ans[-1][1] = x[1]
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
