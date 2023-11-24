from typing import List


class _1st:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        left, right, ans = 0, n - 1, 0
        while left < right:
            if nums[left] + nums[right] >= target:
                right -= 1
            else:
                ans += right - left
                left += 1
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
        nums = [-1, 1, 2, 3, 1]
        target = 2
        handler.countPairs(nums, target)
