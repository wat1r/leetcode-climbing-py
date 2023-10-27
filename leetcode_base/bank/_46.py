from typing import List


class _1st:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = [0] * n

        """
        i 表示当前遍历到的下标
        s 表示可供选择的集合
        """

        def dfs(i, s):
            if i == n:
                ans.append(path.copy())
                return
            for x in s:
                path[i] = x
                dfs(i + 1, s - {x})

        dfs(0, set(nums))
        return ans


class _2nd:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = [0] * n
        on_path = [False] * n

        """
        i 表示当前遍历到的下标
        """

        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return
            for j in range(n):
                if not on_path[j]:
                    on_path[j] = True
                    path[i] = nums[j]
                    dfs(i + 1)
                    on_path[j] = False

        dfs(0)
        return ans


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_1st()]
    for handler in handlers:
        nums = [1, 2, 3]
        handler.permute(nums)
