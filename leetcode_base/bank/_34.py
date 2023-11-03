from typing import List


# 闭区间[left,right]
def lower_bound1(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:  # 区间不为空
        # mid = left + (right - left) // 2
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1  # [mid+1,right]
        else:
            right = mid - 1  # [left,mid-1]
    return left


# 左闭右开[left,right)
def lower_bound2(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums)
    while left < right:  # 区间不为空
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1  # [mid+1,right)
        else:
            right = mid  # [left,mid)
    return left


# 开区间(left,right)
def lower_bound3(nums: List[int], target: int) -> int:
    left = -1
    right = len(nums)
    while left + 1 < right:  # 区间不为空
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid  # (mid,right)
        else:
            right = mid  # (left,mid)
    return right


class _1st:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = lower_bound1(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = lower_bound1(nums, target + 1) - 1
        return [start, end]


class _2nd:
    print("")


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_1st()]
    for handler in handlers:
        nums = [5, 7, 7, 8, 8, 10]
        target = 8
        handler.searchRange(nums, target)
