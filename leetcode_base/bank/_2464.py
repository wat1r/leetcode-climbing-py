from typing import List


class _1st:
    # https://leetcode.cn/problems/next-greater-element-iv/
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        s, t = [], []
        for i, x in enumerate(nums):
            x = nums[i]
            while t and x > nums[t[-1]]:
                ans[t.pop()] = x  # t 栈顶的下下个更大的元素是x
            j = len(s) - 1
            while j >= 0 and nums[s[j]] < x:
                j -= 1  # s 栈顶的下一个更大元素是 x
            t += s[j + 1:]  # 把从 s 弹出的这一整段元素加到 t
            del s[j + 1:]  # 弹出一整段元素
            s.append(i)  # 当前元素（的下标）加到 s 栈顶
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
