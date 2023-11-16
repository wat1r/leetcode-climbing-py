from typing import List


class _1st:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n, m = len(spells), len(potions)
        potions.sort()
        ans = [0] * n
        # 闭区间
        for i in range(0, n):
            x = spells[i]
            l, r = 0, m - 1
            while l < r:
                mid = l + (r - l + 1) // 2
                if potions[mid] * x >= success:
                    r = mid - 1
                else:
                    l = mid
            ans[i] = m - l
            if x * potions[l] < success:
                ans[i] -= 1
        return ans


class _2nd:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n, m = len(spells), len(potions)
        potions.sort()
        ans = [0] * n
        # 开区间
        for i in range(0, n):
            x = spells[i]
            l, r = -1, m
            while l + 1 < r:
                mid = l + (r - l + 1) // 2
                if potions[mid] * x >= success:
                    r = mid
                else:
                    l = mid
            ans[i] = m - l - 1
        return ans


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_2nd()]
    for handler in handlers:
        spells = [3, 1, 2]
        potions = [8, 5, 8]
        success = 16
        handler.successfulPairs(spells, potions, success)
        # spells = [15, 8, 19]
        # potions = [38, 36, 23]
        # success = 328
        # handler.successfulPairs(spells, potions, success)
