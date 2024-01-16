from typing import List


class _1st:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stk = []
        for i in range(2 * n + 1):
            x = nums[i % n]
            while stk and nums[stk[-1]] < x:
                ans[stk.pop()] = x
            stk.append(i % n)
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
        nums = [1, 2, 3, 4, 3]
        handler.nextGreaterElements(nums)
