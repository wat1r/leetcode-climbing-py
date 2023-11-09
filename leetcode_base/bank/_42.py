from typing import List


class _1st:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre_max = [0] * n
        pre_max[0] = height[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], height[i])
        suf_max = [0] * n
        suf_max[-1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            suf_max[i] = max(suf_max[i + 1], height[i])
        ans = 0
        for i, x in enumerate(height):
            ans += min(pre_max[i], suf_max[i]) - height[i]
        return ans


class _2nd:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        left = 0
        right = n - 1
        pre_max = 0
        suf_max = 0
        while left <= right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            if pre_max < suf_max:
                ans += pre_max - height[left]
                left += 1
            else:
                ans += suf_max - height[right]
                right -= 1
        return ans


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_2nd()]
    for handler in handlers:
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        handler.trap(height)
