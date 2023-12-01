from typing import List


class _1st:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        # 左边界left[i]为左侧严格小于arr[i]的最近元素位置(不存在时为-1) 开区间
        left, st = [-1] * n, []
        for i, x in enumerate(arr):
            while st and arr[st[-1]] >= x:
                st.pop()
            if st:
                left[i] = st[-1]
            st.append(i)

        # 右边界right[i]为右侧小于等于arr[i]的最近元素位置(不存在时为n) 开区间
        right, st = [n] * n, []
        for i in range(n - 1, -1, -1):
            while st and arr[st[-1]] > arr[i]:
                st.pop()
            if st:
                right[i] = st[-1]
            st.append(i)

        ans = 0
        for i, (x, l, r) in enumerate(zip(arr, left, right)):
            ans += x * (i - l) * (r - i)
        return ans % (10 ** 9 + 7)


class _2nd:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        # 左边界left[i]为左侧严格小于arr[i]的最近元素位置(不存在时为-1) 开区间
        # 右边界right[i]为右侧小于等于arr[i]的最近元素位置(不存在时为n) 开区间
        left, right, st = [-1] * n, [n] * n, []
        for i, x in enumerate(arr):
            while st and arr[st[-1]] >= x:
                right[st.pop()] = i
            if st:
                left[i] = st[-1]
            st.append(i)
        ans = 0
        for i, (x, l, r) in enumerate(zip(arr, left, right)):
            ans += x * (i - l) * (r - i)
        return ans % (10 ** 9 + 7)


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_1st()]
    for handler in handlers:
        print("")
