from typing import List


class _1st:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        l, r = 0, 0
        ans = 0
        while l < n:
            if nums[l] % 2 == 0:
                r = l
                while r < n - 1 and nums[r] <= threshold and nums[r] % 2 != nums[r + 1] % 2:
                    r += 1
                ans = max(ans, r - l + 1)
            l = r + 1
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
        nums = [3, 2, 5, 4]
        threshold = 5
        handler.longestAlternatingSubarray(nums, threshold)
