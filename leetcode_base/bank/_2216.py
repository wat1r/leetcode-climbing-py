from typing import List


class _1st:
    def minDeletion(self, nums: List[int]) -> int:
        ans = 0
        i, n, start = 1, len(nums), nums[0]  # 先把第一个元素放进去
        odd = True  # 栈大小是否为奇数
        while i < n:
            if odd:  # 此时不能与栈顶的值相同
                if nums[i] == start:
                    ans += 1
                else:
                    odd = False
            else:
                odd = True
                start = nums[i]  # 更新栈顶的元素值
            i += 1
        return ans + (n - ans) % 2


class _2nd:
    print("")


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_1st()]
    for handler in handlers:
        nums = [1, 1, 2, 2, 3, 3]
        handler.minDeletion(nums)
