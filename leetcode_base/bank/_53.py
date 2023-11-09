from typing import List


class _1st:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * n
        f[0] = nums[0]
        ans = f[0]
        for i in range(1, n):
            f[i] = (f[i - 1] + nums[i]) if f[i - 1] > 0 else nums[i]
            ans = max(ans, f[i])
        return ans


class _2nd:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = nums[0]
        ans = cur
        for i in range(1, len(nums)):
            cur = max(nums[i], nums[i] + cur)
            ans = max(ans, cur)
        return ans


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_1st()]
    for handler in handlers:
        print("")
