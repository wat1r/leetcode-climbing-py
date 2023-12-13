from typing import List


class _1st:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {} #dict k:nums2的x，v:nums2中右侧的第一个大于x的值
        stk = []
        for x in reversed(nums2):
            while stk and x > stk[-1]:
                stk.pop()
            res[x] = stk[-1] if stk else -1
            stk.append(x)
        return [res[x] for x in nums1]


class _2nd:
    print("")


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_1st()]
    for handler in handlers:
        nums1 = [4, 1, 2]
        nums2 = [1, 3, 4, 2]
        handler.nextGreaterElement(nums1, nums2)
