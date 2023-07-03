from typing import List


class _1st:
    def combinationSum4(self, nums: List[int], t: int) -> int:
        n = len(nums)
        f = [0] * (t + 1)
        f[0] = 1
        for i in range(0, t + 1):
            for j in range(0, n):
                if nums[j] > i:
                    continue
                print(i, j)
                f[i] += f[i - nums[j]]
        return f[t]


class _2nd:
    def combinationSum4(self, nums: List[int], t: int) -> int:
        n = len(nums)
        f = [0] * (t + 1)
        f[0] = 1
        for i in range(0, t + 1):
            for j in range(0, n):
                if nums[j] > i:
                    break
                print(i, j)
                f[i] += f[i - nums[j]]
        return f[t]


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_1st(), _2nd()]
    for handler in handlers:
        # handler.combinationSum4([1, 2, 3], 4)
        handler.combinationSum4([3, 1, 2, 4], 4)
        print('-------------------------')
